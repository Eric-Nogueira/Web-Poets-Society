# livros/permissions.py
from rolepermissions.permissions import register_object_checker
from permissoes.roles import Administrador

@register_object_checker()
def gerenciar_editora(role, user, editora):
    # Se for um Editor global, pode tudo
    if role == Administrador:
        return True
    
    # Navegação UML: Editora -> responsavel: usuario
    # O usuário pode gerenciar se ele for o responsável cadastrado
    return editora.responsavel == user


@register_object_checker()
def gerenciar_usuario(role, user, perfil_alvo):
    # Se for um Editor global (moderador), pode editar qualquer perfil
    if role == Administrador:
        return True
    
    # Navegação UML: Usuario -> User (django.contrib.auth)
    # Se o usuário logado for o mesmo do perfil alvo
    # Nota: Dependendo de como você ligou o Perfil ao User (OneToOne), 
    # a validação pode ser perfil_alvo.user == user ou apenas perfil_alvo == user.
    # Assumindo que 'perfil_alvo' é o objeto User logado:
    return perfil_alvo == user