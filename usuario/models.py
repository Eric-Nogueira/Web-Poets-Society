from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    Data_Nascimento = models.DateField(null=True, blank=True)
    # Additional fields for the Usuario model can be added here
    
    def __str__(self):
        return self.username