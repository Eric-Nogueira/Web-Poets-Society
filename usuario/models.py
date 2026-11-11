from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    Data_Nascimento = models.DateField(null=True, blank=True)
    # Additional fields for the Usuario model can be added here
    
    class Meta:
            permissions = (
                ("editar_proprio_usuario", "Pode editar o próprio usuário"),
                ("editar_qualquer_usuario", "Pode editar qualquer usuário"),
                ("excluir_proprio_usuario", "Pode excluir o próprio usuário"),
                ("excluir_qualquer_usuario", "Pode excluir qualquer usuário"),
            )
    
    def __str__(self):
        return self.username