from django.db import models

# Create your models here.
class Edicao(models.Model):
    titulo = models.CharField(max_length=100)
    editora = models.ForeignKey('editora.Editora', on_delete=models.CASCADE)
    data_publicacao = models.DateField()
    numero_paginas = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/')
    livro = models.ForeignKey('livros.Livro', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.data_publicacao.year})"