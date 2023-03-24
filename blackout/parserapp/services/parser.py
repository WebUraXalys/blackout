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
from .validator import validate


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
        data = driver.page_source
        return scrap_data(page_data=data)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def scrap_data(page_data):
    soup = BeautifulSoup(page_data, "html.parser")
    page_table = soup.find("table", style="background-color: white;")
    page_tbody = page_table.find_all("tbody")
    data = []
    rows = []
    for tbody in page_tbody:
        tr = tbody.find("tr")
        rows.append(tr)
    for row in rows[1:]:
        other = row.find_all("td")
        buildings = []
        for building in other[3].text.split(", "):
            if building != "":
                buildings.append(building)
        j = {
            'district': row.find("th").text,
            'otg': other[0].text,
            "np": other[1].text,
            "street": other[2].text,
            "buildings": other[3].text,
            "type_off": other[4].text,
            "cause": other[5].text,
            "time_off": other[6].text,
            "time_on": other[7].text
        }
        data.append(j)
    date = soup.find(title="Source Title").text

    # Replace characters from date
    chars = [" ", ".", ":"]
    for el in chars:
        if el != ".":
            date = date.replace(el, "_")
        else:
            date = date.replace(el, "")

    # Following block checks if program started outside of folder parserapp.
    # It's caused by using django management commands
    if "parserapp" in os.listdir():
        prefix = "parserapp/services/"
        if "pages" not in os.listdir(path="parserapp/services/"):  # Checks does directory "pages" exist and create if not
            os.makedirs("parserapp/services/pages")
    else:
        prefix = None
        if "pages" not in os.listdir():
            os.makedirs("pages")

    with open(f"{prefix}pages/{date[1:]}.sjson", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
    return len(data)


def save_data():
    streets_number = 0
    buildings_number = 0
    if "parserapp" in os.listdir():
        path = "parserapp/services/pages"
        files = os.listdir(path=path)
    else:
        path = "pages"
        files = os.listdir(path=path)

    for file in files:
        if ".sjson" not in file:
            files.remove(file)  # Removes all not json files

    for file in files:
        with open(f"{path}/{file}", "r") as json_data:
            data = json.load(json_data)
        for row in data:
            region = row["district"].title()
            otg = row["otg"].title()
            city = row["np"].title()
            street = row["street"].title()
            buildings = row["buildings"]

            interruption = save_interruption(
                cause=row["cause"],
                time_off=row["time_off"],
                time_on=row["time_on"]
            )

            if street != "Не Визначена" or '"' not in street:
                street_id, created = Streets.objects.get_or_create(Name=street, City=city, OTG=otg, Region=region)
                buildings_number = save_buildings(buildings, street_id, interruption)
                print("Added street")
                if created:
                    streets_number += 1
            else:
                print(street)
        if "saved" not in os.listdir(path=path):
            os.makedirs(f"{path}/saved")
        Path(f"{path}/{file}").rename(f"{path}/saved/{file}")

    stats = [streets_number, buildings_number]
    print(f"Parsing finished. Added {streets_number} streets")

    return stats


def save_interruption(cause, time_off, time_on):
    if cause == "ГПВ":
        cause = "Plan"
    else:
        cause = "Emergency"

    month_dict = {
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
    time_off = time_off.split(" ")
    time_off = f"{time_off[0]}/{month_dict[time_off[1]]}/{time_off[2]} {time_off[4]}"
    time_off_obj = datetime.strptime(time_off, '%d/%m/%Y %H:%M')
    time_off_obj = make_aware(time_off_obj)

    time_on = time_on.split(" ")
    time_on = f"{time_on[0]}/{month_dict[time_on[1]]}/{time_on[2]} {time_on[4]}"
    time_on_obj = datetime.strptime(time_on, '%d/%m/%Y %H:%M')
    time_on_obj = make_aware(time_on_obj)

    interruption = Interruptions.objects.create(Start=time_on_obj, End=time_off_obj, Type=cause)

    return interruption


def save_buildings(buildings, street_id, interruption):
    buildings_number = 0
    try:
        buildings = validate(buildings)
    except TypeError:
        print(buildings)
    for building in buildings:
        build, created = Buildings.objects.update_or_create(Address=building, Street=street_id, Interruption=interruption)
        if created:
            buildings_number += 1
    return buildings_number


if __name__ == "__main__":
    print("If you want to run parser, run instead this command: python(3) manage.py parse")
