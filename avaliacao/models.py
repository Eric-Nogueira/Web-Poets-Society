from django.db import models
from django.contrib.auth.models import User


class Avaliacao(models.Model):
    nota = models.TextField(max_length=25)
    comentario = models.TextField()
    data_avaliacao = models.DateField(auto_now_add=True)
    curtida = models.ManyToManyField('auth.User', blank=True, related_name='avaliacoes_curtidas')
    livro = models.ForeignKey('livros.livro', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f' {self.livro.titulo} - {self.nota}'