import datetime
import geocoder
import sqlite3


# Connection to db
connection = sqlite3.connect('../../db.sqlite3')
cur = connection.cursor()


def geocoding_process():
    buildings = cur.execute('SELECT * FROM parserapp_buildings').fetchall()
    number = len(buildings)
    err = 0
    for building in buildings:
        address = cur.execute(
            f'SELECT Name, City FROM parserapp_streets WHERE id = {building[3]}'
        ).fetchone()
        street = address[0]
        city = address[1]
        address = f'{building[1]} {street} вулиця, {city}, Львівська область, Україна'

        success = geocode_addresses(b_id=building[0], address=address)
        if not success:
            err += 1

    print(f'Всього вулиць: {number}\nЗ них не вдалось геокодувати: {err}')

    return number


def geocode_addresses(b_id, address):
    success = False
    g = geocoder.osm(address)

    if g.type is None:
        print(f'Вловив пусту адресу {address}')

    else:
        success = True
        coord = g.latlng
        update_address(long=coord[0], lat=coord[1], b_id=b_id)

    return success


def update_address(long, lat, b_id):
    cur.execute(
        f'UPDATE parserapp_buildings SET Longitude = {long}, Latitude = {lat} WHERE id = {b_id}'
    )
    connection.commit()


if __name__ == '__main__':
    start = datetime.datetime.now()
    count = geocoding_process()
    time = datetime.datetime.now() - start
    print(
        f'Швидкість геокодера: {count / time.total_seconds() * 3600 * 24} записів/день'
    )
