from django.db import models

class Region(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=40,unique=True,blank=True)

    class Meta():
        verbose_name = "Область"
        verbose_name_plural = "Області"
    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(verbose_name="Назва",max_length=40,blank=True)
    city = models.CharField(verbose_name="Місто", max_length=40,blank=True)
    OTG = models.CharField(verbose_name="ОТГ",max_length=40,blank=True)
    region = models.ForeignKey(Region, verbose_name="Регіон",blank=True, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Вулиця"
        verbose_name_plural = "Вулиці"

    def __str__(self):
        return self.name


class Building(models.Model):
    address = models.CharField(verbose_name="Адреса",max_length=40,blank=True)
    street = models.ForeignKey(Street,verbose_name="Вулиця",blank=True, on_delete=models.PROTECT)
    group = models.IntegerField(verbose_name="Група",default=None, blank=True)

    class Meta():
        verbose_name = "Будинок"
        verbose_name_plural = "Будинки"

    def __str__(self):
        return self.address
    

