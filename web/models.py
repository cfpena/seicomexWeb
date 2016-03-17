from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class nosotros_primero(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=400)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
class nosotros_segundo(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=400)
    texto = models.TextField()


    def __str__(self):
        return self.titulo
class nosotros_tercero(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=400)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
class tramite(models.Model):
    titulo = models.CharField(max_length=30)
    referencia = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tramites')

    def __str__(self):              # __unicode__ on Python 2
        return self.titulo

    class Meta:
        ordering = ('titulo',)
class detalle(models.Model):
    fecha = models.DateTimeField('Fecha')
    estado = models.CharField(max_length=50)
    documento = models.FileField(upload_to='documentos', blank=True)
    observacion = models.TextField()
    tramite = models.ForeignKey(tramite, on_delete=models.CASCADE,related_name='detalles')
    def __str__(self):              # __unicode__ on Python 2
        return self.tramite.titulo

    class Meta:
        ordering = ('fecha',)




# Create your models here.
