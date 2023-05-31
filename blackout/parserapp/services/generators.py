from random import randint, choice
from datetime import datetime, timedelta
from ..models import Streets, Interruptions, Buildings
from geopy.geocoders import Nominatim


weekday = datetime.now().isoweekday()
hour = datetime.now().time().hour
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)
interruption_hours = [(0, 1), (1, 5), (5, 9), (9, 13), (13, 17), (17, 21), (21, 23)]
streets_list = ["Проспект свободи", "Проспект Тараса Шевченка", "Галицька площа", "Соборна площа", "Площа ринок", "Площа різні"
                , "Валова вулиця", "Підвальна вул", "Шевська вулиця", "Івана Ґонти вул", "Лесі Українки вул", "Друкарська вул"
                , "Шевська вул", "Краківська вул", "Театральна вул", "Староєврейська вул", "Братів Рогатинців", "Сербська вул"
                , "Валова вул", "Вічева вул", "Проспект В’ячеслава Чорновола", "Академіка Володимира Гнатюка вул", "Северина Наливайка вул"
                , "Торгова вул", "Січових Стрільців вул", "Гетьмана Дорошенка вуд", "Університецька вул", "Листопадового Чину вул"
                , "Степана Бандери вул", "Миколи Коперника вул", "Івана Франка вул", "Під Дубом вул", "Дорошенка вул"
                , "Генерала Тернаського", "Личаківська вул", "Стрийська вул", "Зелена вул", "Під Дубом вул", "Чернівецька вул"
                , "Городоцька вул", "Кульпарківська вул", "Проспект Червоної калини", "Стрийська вул"]


def generate_streets():
    for street_name in streets_list:
        street = Streets(
            Name = street_name,
            City = "Львів",
            OTG = "Львівська",
            Region = "Львів",
            Slug_city = "Львів",
            Slug_street = street_name,
        )
        street.save()

def generate_emergency_interruption():
    emergency_interruption = Interruptions(
        Start=datetime(
            year, month, day, randint(0, hour - 1), randint(0, 59), randint(0, 59)
        ),
        End=datetime(
            year, month, day, randint(hour + 1, 23), randint(0, 59), randint(0, 59)
        ),
        Type="Emergency",
    )
    emergency_interruption.save()


def generate_plan_interruption():
    for start_hour, end_hour in interruption_hours:
        if hour >= start_hour and hour <= end_hour:
            if start_hour == 21 and end_hour == 23:
                plan_interruption = Interruptions(
                    Start=datetime(year, month, day, 21, 0, 0),
                    End=datetime(tomorrow.year, tomorrow.month, tomorrow.day, 1, 0, 0),
                    Type="Plan",
                )
            else:
                plan_interruption = Interruptions(
                    Start=datetime(year, month, day, start_hour, 0, 0),
                    End=datetime(year, month, day, end_hour, 0, 0),
                    Type="Plan",
                )
            plan_interruption.save()
            break


geolocator = Nominatim(user_agent="Blackout")
streets = Streets.objects.all()
buildings = Buildings.objects.all()


def generate_planned_interrupted_buildings():
    plan_interruptions = Interruptions.objects.filter(Type="Plan")
    for street in streets:
        existing_buildings = Buildings.objects.filter(Street=street).order_by('-Address')
        if existing_buildings.exists():
            max_address = existing_buildings.first().Address
        else:
            max_address = 0

        for building in range(max_address + 1, max_address + 1 + randint(32, 78)):
            location = geolocator.geocode(
                str(building) + " " + street.Name + " " + street.City
            )
            if location is not None:
                building_obj = Buildings(
                    Address=building,
                    Street=street,
                    Group=choice(["First", "Second", "Third"]),
                    Interruption=plan_interruptions[0],
                    Longitude=location.longitude,
                    Latitude=location.latitude,
                )
                building_obj.save()
