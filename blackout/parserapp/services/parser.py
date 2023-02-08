from datetime import datetime
from bs4 import BeautifulSoup
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


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
    print(data)
    return data


def save_data(data):
    connection = sqlite3.connect("../../db.sqlite3")
    cur = connection.cursor()
    summary = 0
    streets_number = 0

    for row in data:
        region = row["district"].title()
        otg = row["otg"].title()
        city = row["np"].title()
        street = row["street"].title()
        buildings = row["buildings"]

        exist = cur.execute(
            f"SELECT * FROM parserapp_streets WHERE Name='{street}' AND City='{city}' AND OTG='{otg}';"
        ).fetchall()

        if len(exist) < 1:
            cur.execute(
                f"INSERT INTO parserapp_streets(Name, City, OTG, Region) VALUES('{street}', '{city}', '{otg}', '{region}')"
            )
            connection.commit()
            print(f"{street} додано")
            streets_number += 1

            street_id = cur.lastrowid  # returns id of the last inserted record
            buildings_number = save_buildings(buildings, street_id, cur, connection)
            summary += buildings_number

        else:
            print(f"Вулиця {street} вже є в базі.")
            street_id = exist[0][0]  # exist[0] returns record (id, Name, City, OTG, Region)
            buildings_number = save_buildings(buildings, street_id, cur, connection)
            summary += buildings_number

    counts = [streets_number, summary]
    print(f"Парсинг завершено. Додано {streets_number} вулиць")

    return counts


def save_buildings(buildings, street_id, cur, connection):
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
                cur.execute(f'INSERT INTO parserapp_buildings(Address, Street_id) VALUES("{building}", "{street_id}")')
                connection.commit()
                buildings_number += 1
    return buildings_number


if __name__ == "__main__":
    start = datetime.now()
    driver = start_browser()
    data = get_page(driver)
    counts = save_data(data)
    time = datetime.now() - start
    print(f"Час виконання завдання: {time}")
    print(f"Швидкість запису парсера: {100 / time.total_seconds() * 3600} вул/год")
    print(f"Кількість будинків: {counts[1]}\nШвидкість запису:{counts[1] / time.total_seconds() * 3600} буд/год")


# Following code is written for transforming string into datetime. Now it's unused
# params=time_off.strip().split(' ')
# params2=time_on.strip().split(' ')
#
# day,month_hru,year,gg,time=params
# month_map={
#         "січня":1,
#         "лютого":2,
#         "березня": 3,
#         "квітня": 4,
#         "травня": 5,
#         "червня": 6,
#         "липня": 7,
#         "серпня": 8,
#         "вересня": 9,
#         "жовтня": 10,
#         "листопада": 11,
#         "грудня": 12,
#     }
# time_off_mas=[]
# year=str(year)
# month=str(month_map.get(month_hru))
# day=str(day)
# time=str(time)
# time_off_mas.append((year,"-",month,"-",day,"-",time))
