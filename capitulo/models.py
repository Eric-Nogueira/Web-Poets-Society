from django.db import models

# Create your models here.
from django.db import models

class Capitulo(models.Model):
    titulo = models.CharField(max_length=200)
    num_de_pag = models.IntegerField()
    comentario = models.TextField()
    livro = models.ForeignKey('livros.livro', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo