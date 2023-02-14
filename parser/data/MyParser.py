import requests
from bs4 import BeautifulSoup
import sqlite3
#import csv

header={"User-Agent":
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
}

url="https://poweroff.loe.lviv.ua/search_off?csrfmiddlewaretoken=JdkfijqL9HQXH1XGw2" \
    "nPRQDedd3TBdyFiIlDBgJYIeDHXzh5yyMoZ1Xq4FmuQw4t&city=&street=&otg=&q=%D0%9F%D0%BE%D1%88%D1%83%D0%BA"

response=requests.get(url,headers=header)
soup=BeautifulSoup(response.text,"html.parser")


args=[]

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
conn=sqlite3.connect("database.db")
cursor=conn.cursor()
cursor.executemany("INSERT INTO dataBase "
                   "VALUES (?,?,?,?,?,?,?,?,?)",args)
conn.commit()
conn.close()

#def array():
#    yield (district,otg,city,street,house,type_off,cause,time_off,time_on)
#for item in all_data:
#    print(item.text)

#print(all_data[1].text)'''

