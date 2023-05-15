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
    for plan_interruption in plan_interruptions:    
        for street in streets:
            for building in range(1, randint(32, 78)):
                location = geolocator.geocode(
                    str(building) + " " + street.Name + " " + street.City
                )
                if location is not None:
                    if not Buildings.objects.filter(Address=building, Street=street).exists():
                        building_obj = Buildings(
                            Address=building,
                            Street=street,
                            Group=choice(["First", "Second", "Third"]),
                            Interruption=plan_interruption,
                            Longitude=location.longitude,
                            Latitude=location.latitude,
                        )
                        building_obj.save()
