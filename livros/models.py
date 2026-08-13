from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
