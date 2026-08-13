from django.db import models
from usuario import models as usuario_models

# Create your models here.
class Editora(models.Model):
    endereco = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()
    resposavel = models.ForeignKey(usuario_models.Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.endereco