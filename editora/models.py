from django.db import models
from usuario import models as usuario_models

# Create your models here.
class Editora(models.Model):
    endereco = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()
    resposavel = models.ForeignKey(usuario_models.Usuario, on_delete=models.CASCADE)
    
    class Meta:
            permissions = (
                ("editar_proprio_editora", "Pode editar o próprio editora"),
                ("editar_qualquer_editora", "Pode editar qualquer editora"),
                ("excluir_proprio_editora", "Pode excluir o próprio editora"),
                ("excluir_qualquer_editora", "Pode excluir qualquer editora"),
            )

    def __str__(self):
        return self.endereco