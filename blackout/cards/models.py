from django.db import models
from user.models import User
from parserapp.models import Streets, Buildings


class Cards(models.Model):
    ICON_CHOICES = {
        (1, 'Home'),
        (2, 'Work'),
        (3, 'Gym'),
        (4, 'University'),
        (5, 'Shop'),
        (6, 'Hotel'),
    }
    Title = models.CharField('Title', max_length=15)
    Icon = models.SmallIntegerField('Icon', choices=ICON_CHOICES)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Owner')
    Location = models.ForeignKey(Streets, on_delete=models.CASCADE, related_name='Location')
    Building = models.ForeignKey(Buildings, on_delete=models.CASCADE, related_name='Building_Number')

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return self.Title
