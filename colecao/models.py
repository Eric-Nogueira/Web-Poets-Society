from django.db import models

# Create your models here.

class Colecao(models.Model):
    titulo = models.CharField(max_length=100)
    colecoes_filhas = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='colecoes_pais' )
    
    class Meta:
            permissions = (
                ("editar_proprio_colecao", "Pode editar o próprio coleção"),
                ("editar_qualquer_colecao", "Pode editar qualquer coleção"),
                ("excluir_proprio_colecao", "Pode excluir o próprio coleção"),
                ("excluir_qualquer_colecao", "Pode excluir qualquer coleção"),
            )

    def __str__(self):
        return self.titulo
