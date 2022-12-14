from datetime import datetime
from bs4 import BeautifulSoup
import requests
import orjson

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3"
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
    soup = BeautifulSoup(res.content, features="lxml")
    csrfmiddlewaretoken = soup.find("form", attrs={"action": "/search_off"}).find(attrs={"type": "hidden"}).get("value", None)
    if csrfmiddlewaretoken is None:
        print("Не вдалось витягнути csrfmiddlewaretoken")
        exit()
    res = requests.get(f"https://poweroff.loe.lviv.ua/search_off?csrfmiddlewaretoken={csrfmiddlewaretoken}&city=&street=&otg=&q=%D0%9F%D0%BE%D1%88%D1%83%D0%BA", headers=HEADERS, cookies=csrftoken)
    if not res.ok:
        print(f"Другий запит: {res.status_code}")
        exit()
    return res.content


def scrap_data(page):
    soup = BeautifulSoup(page, features="lxml")
    table = soup.find("table", attrs={"style": "background-color: white;"})
    all_tbody = table.find_all("tbody")
    rows = []
    for tbody in all_tbody:
        tr = tbody.find("tr")
        rows.append(tr)
    print(f"Знайдено {len(rows)} рядків даних")
    data = []
    for row in rows:
        other = row.find_all("td")
        buildings = []
        for building in other[3].text.split(", "):
            if building is not "":
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
            "poweron_time": other[7].text
        }
        data.append(j)
        for x in data:
            print(x["buildings"], end=" ")
            print("")
        #print(data)


def parse():
    page = get_page()
    data = scrap_data(page)
    return data


if __name__ == "__main__":
    start = datetime.now()
    parse()
    end = datetime.now()
    print(f"(parser): Finished in {end - start}")
