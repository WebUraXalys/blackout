from peewee import *  # peewee==3.15.4

# Change path to the database when Django will create its own one
db = SqliteDatabase('../blackout/db.sqlite3')


class BaseModel(Model):
    class Meta:
        database = db


class Region(BaseModel):
    name = CharField()


class Street(BaseModel):
    name = CharField(null=True)
    city = CharField()
    OTG = CharField()
    region = ForeignKeyField(Region, backref="addresses")


class Building(BaseModel):
    address = CharField()
    street = ForeignKeyField(Street, backref="buildings")
    group = IntegerField(null=True)
