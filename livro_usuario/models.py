from django.db import models

class Livro_Usuario(models.Model):
    livro = models.ForeignKey('livros.livro', on_delete=models.CASCADE)
    autor = models.ForeignKey('usuario.usuario', on_delete=models.CASCADE)