from codecs import latin_1_decode
from tabnanny import verbose
from venv import create
from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

class Survivor(Base):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    name = models.CharField(max_length=150,null=False)
    age = models.IntegerField('Idade:',null=False)
    gender = models.CharField('Gênero:',choices=GENDER_CHOICES,null=False, max_length=1)
    latitude = models.FloatField('Latitude:',max_length=100)
    longitude = models.FloatField('Longitude:',max_length=100)
    infected = models.BooleanField('Sobrevivente Infectado?',default=False)
    
    class Meta:
        verbose_name = ('Sobrevivente')
        verbose_name_plural = ('Sobreviventes')
        ordering = ['id']
    
    def __str__(self):
        return self.name

    def get_location(self):
        return '{}, {}'.format(self.latitude, self.longitude)

class Item(Base):
    name = models.CharField('Nome:',max_length=150,null=False)
    points = models.IntegerField('Pontos:',null=False)
    
    class Meta:
        verbose_name = ('Item')
        verbose_name_plural = ('Itens')
        ordering = ['id']
    
    def __str__(self):
        return self.name

class Inventory(models.Model):
    survivor = models.ForeignKey(Survivor, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
    quantity = models.IntegerField('Quantidade:',null=False)
    
    class Meta:
        verbose_name = ('Inventário')
        verbose_name_plural = ('Inventários')
        ordering = ['id']
    
    def __str__(self):
        return self.survivor.name
# Create your models here.
