from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Streets(models.Model):
    Name = models.CharField('Name', max_length=40)
    City = models.CharField('City', max_length=40)
    OTG = models.CharField('OTG', max_length=40)
    Region = models.CharField('Region', max_length=40)

    class Meta:
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'

    def __str__(self):
        return f"{self.Name}"


class Interruptions(models.Model):
    class TypeChoices(models.TextChoices):
        PLAN = "Plan"
        EMERGENCY = "Emergency"

    Start = models.DateTimeField('Start', null=True)
    End = models.DateTimeField('End', null=True)
    Type = models.CharField(
        'Type',
        choices=TypeChoices.choices,
        max_length=10,
        default=TypeChoices.PLAN,
    )

    class Meta:
        verbose_name = 'Interruption'
        verbose_name_plural = 'Interruptions'

    def __str__(self):
        if self.Start and self.End:

            time_start = self.Start.time().strftime('%H:%M')
            time_end = self.End.time().strftime('%H:%M')
            return f"{time_start} - {time_end}"
        return None


class Buildings(models.Model):
    class GroupChoices(models.TextChoices):
        FIRST = "First"
        SECOND = "Second"
        THIRD = 'Third'

    Address = models.CharField('Address', max_length=4)
    Street = models.ForeignKey(
        Streets,
        verbose_name='Street',
        null=True,
        on_delete=models.CASCADE,
    )
    Group = models.CharField(
        'Group',
        max_length=10,
        choices=GroupChoices.choices,
        blank=True,
    )
    Interruption = models.ForeignKey(
        Interruptions,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        default=None,
    )
    Longitude = models.DecimalField(
        max_digits=7,
        decimal_places=5,
        blank=True,
        null=True,
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )
    Latitude = models.DecimalField(
        max_digits=7,
        decimal_places=5,
        blank=True,
        null=True,
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )

    class Meta:
        verbose_name = 'Building'
        verbose_name_plural = 'Buildings'

    def __str__(self):
        return self.Address
