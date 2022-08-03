from calendar import c
from django.contrib import admin
from survivor.models import Survivor

# Register your models here.
@admin.register(Survivor)
class SurvivorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'latitude', 'longitude','infected')
    list_filter = ('name', 'age', 'gender', 'infected')
