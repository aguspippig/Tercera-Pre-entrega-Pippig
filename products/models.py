from django.db import models

# Create your models here.


class Procesador(models.Model):
    marca=models.CharField(max_length=128)
    modelo=models.CharField(max_length=200)
    stock=models.IntegerField()
   
    
    def __str__(self):
        return f'{self.marca} - {self.modelo}'


class PlacaMadre(models.Model):
    marca=models.CharField(max_length=128)
    modelo=models.CharField(max_length=200)
    stock=models.IntegerField()
   
    def __str__(self):
        return f'{self.marca} - {self.modelo}'
        

class Ram(models.Model):
    marca=models.CharField(max_length=128)
    modelo=models.CharField(max_length=200)
    stock=models.IntegerField()
  
    def __str__(self):
        return f'{self.marca} - {self.modelo}'