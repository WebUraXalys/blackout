import os
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
from django.utils.timezone import make_aware
from ..models import Streets, Interruptions, Buildings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import json


MONTHS = {
    "січня": "01",
    "лютого": "02",
    "березня": "03",
    "квітня": "04",
    "травня": "05",
    "червня": "06",
    "липня": "07",
    "серпня": "08",
    "вересня": "09",
    "жовтня": "10",
    "листопада": "11",
    "грудня": "12",
}
DEFAULT_SAVES_DIRECTORY = "/tmp/blk/saves"
SAVED_FOLDER_LOCAL_PATH = "saved"


def get_saves_folder_path():
    path = os.environ.get("BLACKOUT_SAVES", None)
    if path is None:
        print("BLACKOUT_SAVES environment variable is not defined. Define save files folder path in this variable")
        print(f"Default is {DEFAULT_SAVES_DIRECTORY}")
        path = DEFAULT_SAVES_DIRECTORY
    return path


def get_or_create_saved_folder_path(saves_folder):
    saved_dir = os.path.join(saves_folder, SAVED_FOLDER_LOCAL_PATH)
    if not os.path.isdir(saved_dir):
        os.makedirs(saved_dir)
    return saved_dir


def start_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    s = Service(executable_path='path_to_chromedriver')
    driver = webdriver.Chrome(service=s, options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
      '''
    })
    return driver


def get_page(driver):
    url = "https://poweroff.loe.lviv.ua/search_off?csrfmiddlewaretoken=RQrf7SkNXi1AM9WNlaRv50wMeqqoDa5I" \
          "LN7t6S0PNd5eR7zOaXc9Iy5QgxG1mld2&city=&street=&otg=&q=%D0%9F%D0%BE%D1%88%D1%83%D0%BA"
    try:
        driver.get(url)
        time.sleep(10)
        page = driver.page_source
        return page
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def split_buildings(buildings: str):
    building_list = []
    buildings = buildings.split(", ")
    for building in buildings:
        if building != "":
            building_list.append(building)
    return building_list


def parse_poweroff_row(row):
    table_cell = row.find_all("td")

    buildings = split_buildings(table_cell[3].text)

    j = {
        'region': row.find("th").text.title(),
        'otg': table_cell[0].text.title(),
        "city": table_cell[1].text.title(),
        "street": table_cell[2].text.title(),
        "buildings": buildings,
        "type_off": table_cell[4].text,
        "cause": table_cell[5].text,
        "time_off": table_cell[6].text,
        "time_on": table_cell[7].text
    }
    return j


def parse_page_date(page: BeautifulSoup):
    date = page.find(title="Source Title").text

    # Replace characters from date
    chars = [" ", ":"]
    for el in chars:
        date = date.replace(el, "_")
    date = date.replace(".", "")
    return date


def get_poweroffs_table(page):
    page_table = page.find("table", style="background-color: white;")
    return page_table.find_all("tbody")


def get_rows_of_table(table):
    rows = []
    for table_row in table:
        tr = table_row.find("tr")
        rows.append(tr)
    return rows


def parse_poweroff_rows(rows):
    poweroffs = []
    for row in rows:
        data = parse_poweroff_row(row)
        poweroffs.append(data)
    return poweroffs


def scrap_data(page):
    soup = BeautifulSoup(page, "html.parser")
    poweroffs_table = get_poweroffs_table(soup)

    rows = get_rows_of_table(poweroffs_table)
    poweroffs = parse_poweroff_rows(rows)

    date = parse_page_date(soup)
    save_powroffs(poweroffs, date)

    return len(poweroffs)


def save_powroffs(interruptions, date):
    saves_folder = get_saves_folder_path()
    save_file = os.path.join(saves_folder, date[1:] + ".sjson")
    with open(save_file, "w", encoding='utf-8') as f:
        json.dump(interruptions, f, ensure_ascii=False, indent=4)
        f.close()


def get_save_files(saves_folder):
    files = os.listdir(saves_folder)
    files = filter(lambda f: ".sjson" in f, files)  # Filters all not sjson files from list
    return files


def load_json_from_save_file(save_folder, file_name):
    with open(f"{save_folder}/{file_name}", "r") as save_file:
        return json.load(save_file)


def create_interruption_from_save(save):
    interruption = save_interruption(
        cause=save["cause"],
        time_off=save["time_off"],
        time_on=save["time_on"]
    )
    return interruption


def street_name_is_valid(street) -> bool:
    return street != "Не Визначена" and '"' not in street


def create_street_from_save(save) -> int:
    street_name = save["street"]
    if not street_name_is_valid(street_name):
        return 0

    interruption = create_interruption_from_save(save)
    buildings = save["buildings"]
    region = save["region"]
    otg = save["otg"]
    city = save["city"]

    street_id, street_created = Streets.objects.get_or_create(Name=street_name, City=city, OTG=otg, Region=region)
    if street_created:
        buildings_created = save_buildings(buildings, street_id, interruption)
        return buildings_created
    else:
        print(f"Invalid street: {street_name}")
        return 0


def move_file_to_saved(file, saves_folder):
    saved_folder = get_or_create_saved_folder_path(saves_folder)
    before = os.path.join(saves_folder, file)
    after = os.path.join(saved_folder, file)
    os.rename(before, after)


def save_data():
    streets_number = 0
    buildings_number = 0

    saves_folder = get_saves_folder_path()
    save_files = get_save_files(saves_folder)

    for file in save_files:
        saves = load_json_from_save_file(saves_folder, file)
        for save in saves:
            buildings_created = create_street_from_save(save)
            if buildings_created > 0:
                streets_number += 1
                buildings_number += buildings_created

        move_file_to_saved(file, saves_folder)

    stats = [streets_number, buildings_number]
    print(f"Parsing finished. Added {streets_number} streets, and {buildings_number} buildings")

    return stats


def save_interruption(cause, time_off, time_on):
    cause = cause_str_to_objtype(cause)

    start_time = time_str_to_obj(time_on)
    end_time = time_str_to_obj(time_off)

    interruption = Interruptions.objects.create(Start=start_time, End=end_time, Type=cause)

    return interruption


def time_str_to_obj(time_string):
    time_string = time_string.split()
    time_string = f"{time_string[0]}/{MONTHS[time_string[1]]}/{time_string[2]} {time_string[4]}"
    time_obj = datetime.strptime(time_string, '%d/%m/%Y %H:%M')
    return make_aware(time_obj)


def cause_str_to_objtype(cause_str):
    if cause_str == "ГПВ":
        return "Plan"
    else:
        return "Emergency"


def save_buildings(buildings, street_id, interruption):
    buildings_number = 0
    for building in buildings:
        letter = 0
        building = building.replace('"', "")
        for letters in building:
            if letters.isalpha() and letter < 2:  # isalpha method checks is character a letter or not
                letter += 1
        if letter < 2:
            build, created = Buildings.objects.update_or_create(Address=building, Street=street_id, Interruption=interruption)
            if created:
                buildings_number += 1
    return buildings_number


if __name__ == "__main__":
    print("If you want to run parser, run instead this command: python(3) manage.py parse")
