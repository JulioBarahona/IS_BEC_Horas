from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from accounts.models import UserProfile
# Create your models here.

class Actividad (models.Model):
    post = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User)
    canthoras= models.IntegerField(default=0)
    fecha = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    descripcion= models.CharField(max_length=102, default='')
    #integrantes

class Asignacion (models.Model):
  id_actividad = models.ForeignKey(Actividad, null=True, blank=True, on_delete=models.CASCADE)
  id_estudiante = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
