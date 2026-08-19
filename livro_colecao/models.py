from django.db import models

class Livro_Colecao(models.Model):
    livro = models.ForeignKey('livros.livro', on_delete=models.CASCADE)
    colecao = models.ForeignKey('colecao.colecao', on_delete=models.CASCADE)