import pandas
from peewee import *

from models import Street, Building, Region


# Change path to the database when Django will create its own one
db = SqliteDatabase('../blackout/blackout/sqlite3.db')
db.connect()
db.create_tables([Region, Street, Building])

# Uncomment if region isn't in database
# lviv = Region.create(name="Lviv")


group = input("Введіть через пробіл номери груп, які потрібно спарсити: ")
index = group.split()
reg = Region.get(Region.name == "Lviv")


for i in index:
    sheets = pandas.read_excel(f"excel/Grupa_GPV_{i}.xlsx")
    sheet = sheets.dropna(subset=['Вулиця'])  # Excluding rows with empty cell "Street"
    a = 0
    while True:
        try:
            OTG = sheet['ОТГ'].iloc[a]
            town = sheet['Місто'].iloc[a]
            street = sheet['Вулиця'].iloc[a]
            try:
                buildings = sheet['Будинок'].iloc[a]
                buildings_list = buildings.split()
            except:
                buildings_list = []
                buildings_list.append(buildings)
            a += 1

        except:
            break

        info = Street.create(name=street, OTG=OTG, city=town, region=reg)
        for building in buildings_list:
            building = building.replace(',', ' ')
            build = Building.create(address=str(building), street=info, group=i)

        print(f"Запис №{a} внесено до бази даних")
        print('_________________________________________________________________________')
