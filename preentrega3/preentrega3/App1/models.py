from django.db import models

class Guitarra(models.Model):
    nombre=models.CharField(max_length=30)
    color=models.CharField(max_length=30)

class Bajo(models.Model):
    nombre=models.CharField(max_length=30)
    color=models.CharField(max_length=30)

class Bateria(models.Model):
    nombre=models.CharField(max_length=30)
    color=models.CharField(max_length=30)

class Piano(models.Model):
    nombre=models.CharField(max_length=30)
    color=models.CharField(max_length=30)




# Create your models here.
