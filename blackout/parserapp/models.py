from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=40,unique=True)


class Street(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    OTG = models.CharField(max_length=40)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Building(models.Model):
    address = models.CharField(max_length=40)
    street = models.ForeignKey(Street,on_delete=models.PROTECT)
    group = models.IntegerField(default=1)

