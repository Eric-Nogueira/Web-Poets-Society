from django.db import models

# Create your models here.
from django.db import models

class Capitulo(models.Model):
    titulo = models.CharField(max_length=200)
    num_de_pag = models.IntegerField()
    comentario = models.TextField()
    livro = models.ForeignKey('livros.livro', on_delete=models.CASCADE)
    
    class Meta:
            permissions = (
                ("editar_proprio_capitulo", "Pode editar o próprio capítulo"),
                ("editar_qualquer_capitulo", "Pode editar qualquer capítulo"),
                ("excluir_proprio_capitulo", "Pode excluir o próprio capítulo"),
                ("excluir_qualquer_capitulo", "Pode excluir qualquer capítulo"),
            )

    def __str__(self):
        return self.titulo