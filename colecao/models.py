from django.db import models

# Create your models here.

class Colecao(models.Model):
    titulo = models.CharField(max_length=100)
    colecoes_filhas = models.ManyToManyField (
        'self',
        symmetrical=False,
        blank=True,
        related_name='colecoes_pais' )