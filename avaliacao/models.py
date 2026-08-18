from django.db import models

# Create your models here.

class Avaliacao(models.Model):
    nota = models.IntegerField()
    comentario = models.TextField()
    data_avaliacao = models.DateField(auto_now_add=True)
    curtida = models.BooleanField(default=False)
    livro = models.ForeignKey('livros.livro', on_delete=models.CASCADE)