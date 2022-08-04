from django.shortcuts import render
from rest_framework import viewsets
from survivor.serializers import InventorySerializer, ItemSerializer, SurvivorSerializer

from survivor.models import Survivor, Item, Inventory

class SurvivorViewSet(viewsets.ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = ItemSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer