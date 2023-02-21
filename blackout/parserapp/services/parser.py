import os
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import json


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

    if "pages" not in os.listdir():  # Checks does directory "pages" exist and create if not
        os.makedirs("pages")
    with open(f"pages/{date[1:]}.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()

    return data


def save_data():
    connection = sqlite3.connect("../../db.sqlite3")
    cur = connection.cursor()
    summary = 0
    streets_number = 0
    files = os.listdir(path="pages")

    for file in files:
        if ".json" not in file:
            files.remove(file)

    for file in files:
        with open(f"pages/{file}", "r") as json_data:
            data = json.load(json_data)
        for row in data[:10]:
            region = row["district"].title()
            otg = row["otg"].title()
            city = row["np"].title()
            street = row["street"].title()
            buildings = row["buildings"]

            interruption = save_interruption(
                cause=row["cause"],
                time_off=row["time_off"],
                time_on=row["time_on"],
                cur=cur,
                con=connection
            )

            exist = cur.execute(
                f"SELECT * FROM parserapp_streets WHERE Name='{street}' AND City='{city}' AND OTG='{otg}';"
            ).fetchall()

            if len(exist) < 1:
                cur.execute(
                    f"INSERT INTO parserapp_streets(Name, City, OTG, Region) VALUES('{street}', '{city}', '{otg}', '{region}')"
                )
                connection.commit()
                print(f"{street} added")
                streets_number += 1

                street_id = cur.lastrowid  # returns id of the last inserted record
                buildings_number = save_buildings(buildings, street_id, cur, connection, interruption)
                summary += buildings_number

            else:
                print(f"Street {street} already exist.")
                street_id = exist[0][0]  # exist[0] returns record (id, Name, City, OTG, Region)
                buildings_number = save_buildings(buildings, street_id, cur, connection, interruption)
                summary += buildings_number

        if "saved" not in os.listdir(path="pages"):
            os.makedirs("pages/saved")
        Path(f"pages/{file}").rename(f"pages/saved/{file}")

    counts = [streets_number, summary]
    print(f"Parsing finished. Added {streets_number} streets")

    return counts


def save_interruption(cause, time_off, time_on, cur, con):
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

    time_on = time_on.split(" ")
    time_on = f"{time_on[0]}/{month_dict[time_on[1]]}/{time_on[2]} {time_on[4]}"
    time_on_obj = datetime.strptime(time_off, '%d/%m/%Y %H:%M')
    cur.execute(
        f"INSERT INTO parserapp_interruptions(Start, End, Type) VALUES('{time_on_obj}', '{time_off}', '{cause}')"
    )
    con.commit()
    interruption_id = cur.lastrowid
    return interruption_id


def save_buildings(buildings, street_id, cur, connection, interruption):
    buildings_number = 0
    buildings = buildings.split(",")
    for building in buildings:
        letter = 0
        building = building.replace('"', "")
        for letters in building:
            if letters.isalpha() and letter < 2:  # isalpha method checks
                letter += 1
        if letter < 2:
            exist = cur.execute(f'SELECT * FROM parserapp_buildings WHERE Address="{building}" and Street_id="{street_id}"').fetchall()
            if len(exist) < 1:
                cur.execute(f'INSERT INTO parserapp_buildings(Address, Street_id, Interruption_id) VALUES("{building}", "{street_id}", "{interruption}")')
                connection.commit()
                buildings_number += 1
            else:
                cur.execute(f'UPDATE parserapp_buildings '
                            f'SET Interruption_id = {interruption} '
                            f'WHERE id="{exist[0][0]}"')
                connection.commit()
    return buildings_number


if __name__ == "__main__":
    start = datetime.now()
    driver = start_browser()
    get_page(driver)
    counts = save_data()
    time = datetime.now() - start
    print(f"Time of working: {time}")
    print(f"Parser recording speed: {100 / time.total_seconds() * 3600} streets per hour")
    print(f"Count of buildings: {counts[1]}\nRecording speed:{counts[1] / time.total_seconds() * 3600} buildings per hour")
