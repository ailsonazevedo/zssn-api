from codecs import latin_1_decode
from tabnanny import verbose
from venv import create
from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

class Survivor(Base):
    #Um sobrevivente deve ter um nome, idade, sexo e último local (latitude,longitude).
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    name = models.CharField(max_length=150,null=False)
    age = models.IntegerField('Idade:',null=False)
    gender = models.CharField('Gênero:',choices=GENDER_CHOICES,null=False, max_length=1)
    latitude = models.FloatField('Latitude:',max_length=50)
    longitude = models.FloatField('Longitude:',max_length=50)
    infected = models.BooleanField('Infectado', default=False)
    
    class Meta:
        verbose_name = ('Sobrevivente')
        verbose_name_plural = ('Sobreviventes')
        ordering = ['id']
    
    def __str__(self):
        return self.name


# Create your models here.
