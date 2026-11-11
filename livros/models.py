from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    
    class Meta:
        permissions = (
            ("editar_proprio_livro", "Pode editar o próprio livro"),
            ("editar_qualquer_livro", "Pode editar qualquer livro"),
            ("excluir_proprio_livro", "Pode excluir o próprio livro"),
            ("excluir_qualquer_livro", "Pode excluir qualquer livro"),
        )

    def __str__(self):
        return self.titulo
