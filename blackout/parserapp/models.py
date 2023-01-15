from django.db import models

class Streets(models.Model):
    Name = models.CharField('Name',max_length=40)
    City = models.CharField('City', max_length=40)
    OTG = models.CharField('OTG',max_length=40)
    Region = models.CharField('Region', max_length=40)

    class Meta():
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'

    def __str__(self):
        return self.Name

class Interruptions(models.Model):
    type_choices = [
        ('0', 'Plan'),
        ('1', 'Emergency')
    ]


    Start = models.DateTimeField('Start',null=True)
    End = models.DateTimeField('End',null=True)
    Type = models.CharField('Type', choices=type_choices, max_length=1, default=type_choices[0])

    class Meta():
        verbose_name = 'Interruption'
        verbose_name_plural = 'Interruptions'

class Buildings(models.Model):
    group_choices = [
        ('1','First'),
        ('2','Second'),
        ('3','Third'),
    ]

    Address = models.CharField('Address', max_length=4)
    Street = models.ForeignKey(Streets, verbose_name='Street', null=True, on_delete=models.CASCADE)
    Group = models.CharField('Group',max_length=1, choices=group_choices, blank=True)
    Interruption = models.ForeignKey(Interruptions,blank=True,null=True, on_delete=models.CASCADE)
        
    class Meta():
        verbose_name = 'Building'
        verbose_name_plural = 'Buildings'

    def __str__(self):
        return self.Address
