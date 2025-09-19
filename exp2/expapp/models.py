from django.db import models
from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_name = models.CharField(max_length=255, help_text="Car name")
    car_model = models.CharField(max_length=100, help_text="Car Model")
    mileage = models.IntegerField(help_text="FC Date")
    car_ins_date = models.DateField(max_length=50, help_text="Insurance Date")
    rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Car Rating (e.g., 8.5)")
    
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'mileage', 'car_ins_date', 'rating')

