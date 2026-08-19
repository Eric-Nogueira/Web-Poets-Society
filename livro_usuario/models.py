from django.db import models

class Livro_Usuario(models.Model):
    livro = models.ForeignKey('Livros.Livro', on_delete=models.CASCADE)
    autor = models.ForeignKey('Usuario.Usuario', on_delete=models.CASCADE)