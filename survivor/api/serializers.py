from rest_framework import serializers, viewsets, routers
from ..models import Survivor, Item, Inventory

class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ['id','name', 'age', 'gender', 'infected', 'latitude', 'longitude','get_location']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name', 'points']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id','survivor', 'item', 'quantity']