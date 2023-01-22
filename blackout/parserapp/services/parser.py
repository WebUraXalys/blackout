from datetime import datetime
from bs4 import BeautifulSoup
import requests
import orjson
from celery import shared_task
import sqlite3
from datetime import datetime
#from blackout.celery import app

from blackout.parserapp.models import Region, Street, Building

'''HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3"
}'''


header={"User-Agent":
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
}

url="https://poweroff.loe.lviv.ua/search_off?csrfmiddlewaretoken=JdkfijqL9HQXH1XGw2" \
    "nPRQDedd3TBdyFiIlDBgJYIeDHXzh5yyMoZ1Xq4FmuQw4t&city=&street=&otg=&q=%D0%9F%D0%BE%D1%88%D1%83%D0%BA"

response=requests.get(url,headers=header)
soup=BeautifulSoup(response.text,"html.parser")


args=[]

time_update=soup.find("cite",title="Source Title").text
data = soup.find("div",style="overflow-x:auto;").find_all("tbody")


for item in data:
    full_data=item.find_all("td")
    district_data = item.find_all("th")

    district = (district_data[0].text)
    otg=(full_data[0].text)
    city=(full_data[1].text)
    street=(full_data[2].text)
    house=(full_data[3].text)
    type_off=(full_data[4].text)
    cause=(full_data[5].text)
    time_off=(full_data[6].text)
    time_on=(full_data[7].text)

    args.append((district,otg,city,street,house,type_off,cause,time_off,time_on))
print(args)
time_now=datetime.now()
conn=sqlite3.connect("Data.db")
cursor=conn.cursor()
cursor.executemany("INSERT INTO base VALUES (?,?,?,?,?,?,?,?,?)",args)
conn.commit()
conn.close()
print("Час оновлення даних на сайті:",time_update,"\nЧас початку парсинга",time_now)



'''def get_page():
    res = requests.get("https://poweroff.loe.lviv.ua/", headers=HEADERS)
    if not res.ok:
        print(f"Перший запит: {res.status_code}")
        exit()
    csrftoken = res.cookies
    if csrftoken is None:
        print("Не вдалось витягнути csrftoken")
        exit()
    soup = BeautifulSoup(res.content, features="html.parser")
    csrfmiddlewaretoken = soup.find("form", attrs={"action": "/search_off"}).find(attrs={"type": "hidden"}).get("value", None)
    if csrfmiddlewaretoken is None:
        print("Не вдалось витягнути csrfmiddlewaretoken")
        exit()
    res = requests.get(f"https://poweroff.loe.lviv.ua/search_off?csrfmiddlewaretoken={csrfmiddlewaretoken}&city=&street=&otg=&q=%D0%9F%D0%BE%D1%88%D1%83%D0%BA", headers=HEADERS, cookies=csrftoken)
    if not res.ok:
        print(f"Другий запит: {res.status_code}")
        exit()
    return res.content'''


'''def scrap_data(page):
    soup = BeautifulSoup(page, features="html.parser")
    table = soup.find("table", attrs={"style": "background-color: white;"})
    all_tbody = table.find_all("tbody")
    rows = []
    for tbody in all_tbody:
        tr = tbody.find("tr")
        rows.append(tr)
    print(f"Знайдено {len(rows)} рядків даних")
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
            "poweron_time": other[7].text
        }


        #data.append(j)
        # for x in data:
        #     print(x["buildings"], end=" ")
        #     print("")
    #print(data)

    return data'''


'''def parse():
    page = get_page()
    data = scrap_data(page)
    return data'''


def save_data(args):
    try:
        region = Region.objects.get(name="Lviv")
    except:
        region = Region.objects.create(name="Lviv")
    for x in args:
        otg = x['otg']
        city = x['np']
        street = x['street']
        try:
            street = Street.objects.get(city=city, OTG=otg, name=street)
            print(f"Вулиця {street.name} вже є в базі.")
        except:
            street = Street.objects.create(name=street, city=city, OTG=otg, region=region)
            street = Street.objects.get(name=street, city=city, OTG=otg, region=region)
            print(f"Вулицю {street.name} додано.")
        buildings=x['buildings']
        save_buildings(buildings, street)
    message = f"Парсинг завершено. Додано {args.count()} вулиць"
    return message




def save_buildings(buildings, street):
    for building in buildings:
        try:
            structure = Building.objects.get(address=building, street=street)
        except:
            structure = Building.objects.create(address=building, street=street)

'''

# @app.task(bind=True)

def parsing_process():
    data = parse()
    message = save_data(data)
    return message


if __name__ == "__main__":
    start = datetime.now()
    parsing_process()
    end = datetime.now()
    print(f"(parser): Finished in {end - start}")'''
