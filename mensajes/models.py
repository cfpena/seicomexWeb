from __future__ import unicode_literals

from django.db import models

class mensaje(models.Model):
    titulo = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    asunto = models.CharField(max_length=1000)
    texto = models.TextField()

# Create your models here.
