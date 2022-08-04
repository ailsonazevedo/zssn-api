from calendar import c
from django.contrib import admin
from survivor.models import Inventory, Survivor, Item

@admin.register(Survivor)
class SurvivorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'latitude', 'longitude','infected', 'get_location')
    list_filter = ('name', 'age', 'gender', 'infected')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'points')
    list_filter = ('name', 'points')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('survivor', 'quantity')
    list_filter = ('survivor', 'item')