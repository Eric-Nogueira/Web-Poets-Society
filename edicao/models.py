from django.db import models

class Edicao(models.Model):
    titulo = models.CharField(max_length=100)
    editora = models.ForeignKey('editora.Editora', on_delete=models.CASCADE)
    data_publicacao = models.DateField()
    numero_paginas = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/', blank=True)
    livro = models.ForeignKey('livros.Livro', on_delete=models.CASCADE)
    
    class Meta:
            permissions = (
                ("editar_proprio_edicao", "Pode editar o próprio edição"),
                ("editar_qualquer_edicao", "Pode editar qualquer edição"),
                ("excluir_proprio_edicao", "Pode excluir o próprio edição"),
                ("excluir_qualquer_edicao", "Pode excluir qualquer edição"),
            )

    def __str__(self):
        return f"{self.titulo} ({self.data_publicacao.year})"