from random import randint
from datetime import datetime, timedelta
from ..models import Streets, Interruptions, Buildings


weekday = datetime.now().isoweekday()
hour = datetime.now().time().hour
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)

def generate_interruptions():
    emergency_interruption = Interruptions(Start = datetime(year, month, day, randint(0,hour-1), randint(0,59), randint(0,59)),End = datetime(year, month, day, randint(hour+1,23), randint(0,59), randint(0,59)),Type = "Emergency")
    emergency_interruption.save()
    if hour >= 0 and hour <= 1:
        plan_interruption = Interruptions(Start = datetime(year, month, yesterday.day, 21, 0, 0),End = datetime(year, month, day, 1, 0, 0),Type = "Plan")
        plan_interruption.save()
    elif hour >= 1 and hour <= 5:
        plan_interruption = Interruptions(Start = datetime(year, month, day, 1, 0, 0),End = datetime(year, month, day, 5, 0, 0),Type = "Plan")
        plan_interruption.save()
    elif hour >= 5 and hour <= 9:
        plan_interruption = Interruptions(Start = datetime(year, month, day, 5, 0, 0),End = datetime(year, month, day, 9, 0, 0),Type = "Plan")
        plan_interruption.save()
    elif hour >= 9 and hour <= 13:
        plan_interruption = Interruptions(Start = datetime(year, month, day, 9, 0, 0),End = datetime(year, month, day, 13, 0, 0),Type = "Plan")
        plan_interruption.save()
    elif hour >= 13 and hour <= 17:
        plan_interruption = Interruptions(Start = datetime(year, month, day, 13, 0, 0),End = datetime(year, month, day, 17, 0, 0),Type = "Plan")
        plan_interruption.save()
    elif hour >= 17 and hour <= 21:
        plan_interruption = Interruptions(Start = datetime(year, month, day, 17, 0, 0),End = datetime(year, month, day, 21, 0, 0),Type = "Plan")
        plan_interruption.save()
    elif hour >= 21 and hour <= 23:
        plan_interruption = Interruptions(Start = datetime(year, month, day, 21, 0, 0),End = datetime(year, month, tomorrow.day, 1, 0, 0),Type = "Plan")
        plan_interruption.save()
