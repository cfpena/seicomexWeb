from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class tramite(models.Model):
    titulo = models.CharField(max_length=30)
    referencia = models.CharField(max_length=12)
    users =models.ManyToManyField(User,blank=True, null=True, related_name='tramites')

    def __str__(self):              # __unicode__ on Python 2
        return self.titulo

    class Meta:
        ordering = ('titulo',)
class detalle(models.Model):
    fecha = models.DateTimeField('Fecha')
    estado = models.CharField(max_length=50)
    documento = models.FileField(upload_to='documentos', blank=True)
    observacion = models.CharField(max_length=100, blank=True)
    tramite = models.ForeignKey(tramite, on_delete=models.CASCADE,related_name='detalles')
    def __str__(self):              # __unicode__ on Python 2
        return self.tramite.titulo

    class Meta:
        ordering = ('fecha',)




# Create your models here.
