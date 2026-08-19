from django.db import models

class Livro_Colecao(models.Model):
    livro = models.ForeignKey('Livros.Livro', on_delete=models.CASCADE)
    colecao = models.ForeignKey('Colecao.Colecao', on_delete=models.CASCADE)