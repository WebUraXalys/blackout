import os, time, json
from datetime import datetime
from bs4 import BeautifulSoup
from django.utils.timezone import make_aware
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from blackout.settings import BASE_DIR
from ..models import Streets, Interruptions, Buildings
from .validator import validate


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
DEFAULT_SAVES_DIRECTORY = str(BASE_DIR.parent.joinpath('tmp'))
if not os.path.isdir(DEFAULT_SAVES_DIRECTORY):
    os.makedirs(DEFAULT_SAVES_DIRECTORY+'/saved/')


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
    return [build for build in buildings.split(", ") if build != ""]

def parse_poweroff_row(row):
    table_cell = row.find_all("td")
    buildings = split_buildings(table_cell[3].text)

    return {
        "region": row.find("th").text.title(),
        "otg": table_cell[0].text.title(),
        "city": table_cell[1].text.title(),
        "street": table_cell[2].text.title(),
        "buildings": buildings,
        "type_off": table_cell[4].text,
        "time_off": table_cell[5].text,
        "time_on": table_cell[6].text
    }


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


def scrap_data(page):
    soup = BeautifulSoup(page, "html.parser")
    poweroffs_table = get_poweroffs_table(soup)

    rows = [row.find("tr") for row in poweroffs_table]
    poweroffs = list(map(parse_poweroff_row, rows))

    date = parse_page_date(soup)
    save_powroffs(poweroffs, date)

    return len(poweroffs)


def save_powroffs(interruptions, date):
    file = f"{DEFAULT_SAVES_DIRECTORY}/{date[1:]}.json"
    with open(file, "w", encoding='utf-8') as f:
        json.dump(interruptions, f, ensure_ascii=False, indent=4)



def get_save_files(saves_folder):
    files = os.listdir(saves_folder)
    files = filter(lambda f: ".json" in f, files)  # Filters all not json files from list
    return files


def create_interruption_from_save(save):
    interruption = save_interruption(
        time_off=save["time_off"],
        time_on=save["time_on"]
    )
    return interruption


def street_name_is_valid(street) -> bool:
    return street != "Не Визначена" or '"' not in street


def create_street_from_save(save) -> int:
    street_name = save["street"]
    if not street_name_is_valid(street_name):
        return 0

    interruption = create_interruption_from_save(save)
    buildings = validate(save["buildings"])
    region = save["region"]
    otg = save["otg"]
    city = save["city"]

    street_id, street_created = Streets.objects.get_or_create(Name=street_name, City=city, OTG=otg, Region=region)
    if street_created:
        return save_buildings(buildings, street_id, interruption)
    else:
        print(f"Invalid street: {street_name}")
        return 0


def move_file_to_saved(file_name):
    temp_file = f"{DEFAULT_SAVES_DIRECTORY}/{file_name}"
    saves_folder = f"{DEFAULT_SAVES_DIRECTORY}/saved/{file_name}"
    os.rename(temp_file, saves_folder)


def save_data():
    streets_number = 0
    buildings_number = 0

    saves_folder = DEFAULT_SAVES_DIRECTORY
    save_files = get_save_files(saves_folder)

    for file_name in save_files:
        with open(f"{saves_folder}/{file_name}", "r", encoding='utf-8') as save_file:
            json_file = json.load(save_file)

            for save in json_file:
                buildings_created = create_street_from_save(save)
                if buildings_created > 0:
                    streets_number += 1
                    buildings_number += buildings_created

        move_file_to_saved(file_name)

    print(f"Parsing finished. Added {streets_number} streets, and {buildings_number} buildings")

    return [streets_number, buildings_number]


def save_interruption(time_off, time_on):
    start_time = time_str_to_obj(time_on)
    end_time = time_str_to_obj(time_off)
    interruption = Interruptions.objects.create(Start=start_time, End=end_time)
    return interruption


def time_str_to_obj(time_string):
    time_string = time_string.split()
    time_string = f"{time_string[0]}/{MONTHS[time_string[1]]}/{time_string[2]} {time_string[4]}"
    time_obj = datetime.strptime(time_string, '%d/%m/%Y %H:%M')
    return make_aware(time_obj)


def save_buildings(buildings, street_id, interruption):
    buildings_number = 0

    for building in buildings:
        _, created = Buildings.objects.update_or_create(Address=building, Street=street_id, Interruption=interruption)
        if created:
            buildings_number += 1
    return buildings_number


if __name__ == "__main__":
    print("If you want to run parser, run instead this command: python(3) manage.py parse")
