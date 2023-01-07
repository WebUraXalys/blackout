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
    if i != "3":
        sheet = table.dropna(subset=['Вулиця'])  # Excluding rows with empty cell "Street"
    else:
        sheet = table  # Third group has cells where cities don't have streets but are represented by single row

    a = 0
    if i == "3":
        buildings_list = []
        while True:
            try:
                OTG = sheet['ОТГ'].iloc[a]
                city = sheet['Місто'].iloc[a]
                street = sheet['Вулиця'].iloc[a]
            except:
                break
            try:
                street_list = street.split()
                for s in street_list:
                    s = s.replace(",", " ")
                    try:
                        # Looking for existing record in DB
                        record = Street.get(Street.name == s, Street.OTG == OTG, Street.city == city, Street.region == reg)
                    except:
                        # Creating new record
                        record = Street.create(name=s, OTG=OTG, city=city, region=reg)
            except:
                record = Street.create(OTG=OTG, city=city, region=reg)
                    

            a += 1
            print(f"Запис №{a} внесено до бази даних")
            print('_________________________________________________________________________')
    else:
        while True:
            buildings_list = []
            try:
                OTG = sheet['ОТГ'].iloc[a]
                city = sheet['Місто'].iloc[a]
                street = sheet['Вулиця'].iloc[a]
                try:
                    buildings = sheet['Будинок'].iloc[a]  # This cell might be empty
                    buildings_list = buildings.split()
                except:
                    buildings_list.append(buildings)
                a += 1

            except:
                break

            try:
                # Looking for existing record in DB
                record = Street.get(Street.name == street, Street.OTG == OTG, Street.city == city, Street.region == reg)
            except:
                # Creating new record
                record = Street.create(name=street, OTG=OTG, city=city, region=reg)

            for building in buildings_list:
                building = str(building).replace(',', ' ')
                try:
                    # Looking for existing record in DB and updating it
                    structure = Building.get(Building.address == str(building), Building.street == record)
                    structure.group = i
                    structure.save()
                except:
                    # Creating new record
                    structure = Building.create(address=building, street=record, group=i)

            print(f"Запис №{a} внесено до бази даних")
            print('_________________________________________________________________________')
