from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Table(models.Model):
        table_number = models.IntegerField(primary_key=True, null=False, blank=False)
        number_of_seats = models.IntegerField(null=False, blank=False)

class Reservation(models.Model):
        id = models.CharField(max_length=10, primary_key=True, null=False, blank=False)
        table_number = models.ForeignKey(Table, on_delete=models.DO_NOTHING)
        first_name = models.CharField(max_length=50, null=False, blank=False)
        last_name = models.CharField(max_length=50, null=False, blank=False)
        email_address = models.CharField(max_length=100, null=False, blank=False)
        number_of_people = models.IntegerField(
                validators=[
                        MaxValueValidator(6),
                        MinValueValidator(1)
                ], 
                null=False, 
                blank=False
        )
        date = models.DateField(null=False, blank=False)
        time = models.TimeField(null=False, blank=False)



def __str__(self):
        return self.name



