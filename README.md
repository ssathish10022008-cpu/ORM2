# Ex02 Django ORM Web Application
## Date:18.09.2025 

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
models.py
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
admin.py
from django.contrib import admin
from.models import Car,CarAdmin
admin.site.register(Car,CarAdmin)   
```    


## OUTPUT
![alt text](<Screenshot 2025-09-15 114445.png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
