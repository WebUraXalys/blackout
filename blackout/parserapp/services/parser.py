from datetime import datetime
from bs4 import BeautifulSoup
import requests
import sqlite3


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3",
}


def get_page():
    res = requests.get("https://poweroff.loe.lviv.ua/", headers=HEADERS)
    if not res.ok:
        print(f"Перший запит: {res.status_code}")
        exit()
    csrftoken = res.cookies
    if csrftoken is None:
        print("Не вдалось витягнути csrftoken")
        exit()
    soup = BeautifulSoup(res.content, features="html.parser")
    csrfmiddlewaretoken = (
        soup.find("form", attrs={"action": "/search_off"})
        .find(attrs={"type": "hidden"})
        .get("value", None)
    )
    if csrfmiddlewaretoken is None:
        print("Не вдалось витягнути csrfmiddlewaretoken")
        exit()
    res = requests.get(
        f"https://poweroff.loe.lviv.ua/search_off?csrfmiddlewaretoken={csrfmiddlewaretoken}&city=&street=&otg=&q=%D0%9F%D0%BE%D1%88%D1%83%D0%BA",
        headers=HEADERS,
        cookies=csrftoken,
    )
    if not res.ok:
        print(f"Другий запит: {res.status_code}")
        exit()
    return res.content


def scrap_data(page):
    soup = BeautifulSoup(page, features="html.parser")
    time_update = soup.find(
        "cite", title="Source Title"
    ).text  # Might be useful in the future
    table = soup.find("table", attrs={"style": "background-color: white;"})
    all_tbody = table.find_all("tbody")
    rows = []
    for tbody in all_tbody:
        tr = tbody.find("tr")
        rows.append(tr)
    print(f"Знайдено {len(rows)} рядків даних")
    print(time_update)
    data = []
    for row in rows[1:]:
        other = row.find_all("td")
        buildings = []
        for building in other[3].text.split(", "):
            if building != "":
                buildings.append(building)
        j = {
            "district": row.find("th").text,
            "otg": other[0].text,
            "np": other[1].text,
            "street": other[2].text,
            "buildings": buildings,
            "poweroff_type": other[4].text,
            "poweroff_cause": other[5].text,
            "poweroff_time": other[6].text,
            "poweron_time": other[7].text,
        }
        data.append(j)

    return data


def parse():
    page = get_page()
    data = scrap_data(page)
    return data


def save_data(data):
    connection = sqlite3.connect("../../db.sqlite3")
    cur = connection.cursor()

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

            street_id = cur.lastrowid  # returns id of the last inserted record
            save_buildings(buildings, street_id, cur, connection)

        else:
            print(f"Вулиця {street} вже є в базі.")
            street_id = exist[0][
                0
            ]  # exist[0] returns record (id, Name, City, OTG, Region)
            save_buildings(buildings, street_id, cur, connection)

    connection.close()
    message = f"Парсинг завершено. Додано {len(data)} вулиць"

    return message


def save_buildings(buildings, street_id, cur, connection):
    for building in buildings:
        letter = 0
        for letters in building:
            if building[letters].isalpha():  # isalpha method checks
                letter += 1
        if letter < 2:
            exist = cur.execute(
                f'SELECT * FROM parserapp_buildings WHERE Address="{building}" and Street_id="{street_id}"'
            ).fetchall()
            if len(exist) < 1:
                cur.execute(
                    f'INSERT INTO parserapp_buildings(Address, Street_id) VALUES("{building}", "{street_id}"'
                )
                connection.commit()


def saving():
    data = parse()
    message = save_data(data)
    return message


if __name__ == "__main__":
    start = datetime.now()
    saving()
    time = datetime.now() - start
    print(f"Швидкість геокодера: {100 / time.total_seconds() * 3600 * 24}")


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
