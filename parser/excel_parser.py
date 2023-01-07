import pandas
from peewee import *

from models import Street, Building, Region, db

group = input("Введіть через пробіл номери груп, які потрібно спарсити: ")
index = group.split()

db.connect()
db.create_tables([Region, Street, Building])

if Region.select(Region.name == "Lviv").count() < 1:
    reg = Region.create(name="Lviv")
else:
    reg = Region.get(name="Lviv")

for i in index:
    table = pandas.read_excel(f"excel/Grupa_GPV_{i}.xlsx")
    sheet = table.dropna(subset=['Вулиця'])  # Excluding rows with empty cell "Street"

    a = 0
    while True:
        buildings_list = []
        if i == 3:
            try:
                OTG = sheet['ОТГ'].iloc[a]
                city = sheet['Місто'].iloc[a]
                street = sheet['Вулиця'].iloc[a]
            except:
                break
            street_list = street.split()
            a += 1
            for s in street_list:
                try:
                    # Looking for existing record in DB
                    record = Street.get(Street.name == s, Street.OTG == OTG, Street.city == city, Street.region == reg)
                except:
                    # Creating new record
                    record = Street.create(name=s, OTG=OTG, city=city, region=reg)

        print(f"Запис №{a} внесено до бази даних")
        print('_________________________________________________________________________')
