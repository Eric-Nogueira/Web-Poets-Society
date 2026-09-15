from django.db import models

# Create your models here.
class Edicao(models.Model):
    titulo = models.CharField(max_length=100)
    editora = models.ForeignKey('editora.Editora', on_delete=models.CASCADE)
    data_publicacao = models.DateField()
    numero_paginas = models.IntegerField()
    # Sem blank=True o campo era obrigatorio no model mas ficava de fora
    # do formulario, entao a edicao era salva com o PDF vazio na marra.
    pdf = models.FileField(upload_to='pdfs/', blank=True)
    livro = models.ForeignKey('livros.Livro', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.data_publicacao.year})"