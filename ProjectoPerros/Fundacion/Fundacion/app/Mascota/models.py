from django.db import models

# Create your models here.


class Mascota(models.Model):
	 foto = models.TextField()
	 nombre = models.CharField(max_length=50)
	 raza = models.CharField(max_length=50)
	 descripcion = models.CharField(max_length=50)
	 estado = models.CharField(max_length=50)



class Dueño(models.Model):
	correo = models.CharField(max_length=50)
	run = models.CharField(max_length=12)
	nombre = models.CharField(max_length=100)
	fecha = models.DateField()
	telefono = models.IntegerField()
	region = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
