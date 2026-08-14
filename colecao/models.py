from django.db import models

# Create your models here.

class Colecao(models.Model):
    titulo = models.CharField(max_length=100)