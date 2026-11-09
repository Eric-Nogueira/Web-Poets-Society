from rolepermissions.permissions import register_object_checker
from permissoes.roles import Administrador
from livro_usuario.models import LivroUsuario

@register_object_checker()
def gerenciar_livro(role, user, livro):
    if role == Administrador:
        return True  
    
    e_autor_do_livro = LivroUsuario.objects.filter(livro=livro, autor=user).exists()
    if e_autor_do_livro:
        return True
    
    return False  

@register_object_checker()
def gerenciar_capitulo(role, user, capitulo):
    # Regra: Se for Editor, pode tudo.
    if role == Administrador:
        return True
    
    # Navegação UML: Capitulo -> Livro -> Livro_Usuario -> Usuario
    # O usuário pode gerenciar o capítulo se ele for autor do livro do capítulo.
    return LivroUsuario.objects.filter(livro=capitulo.livro, autor=user).exists()


@register_object_checker()
def gerenciar_colecao(role, user, colecao):
    if role == Administrador:
        return True  
    
    return LivroUsuario.objects.filter(
        livro__livro_colecao__colecao=colecao, # Segue a relação da classe associativa
        autor=user
    ).exists()
    

@register_object_checker()
def gerenciar_avaliacao(role, user, avaliacao):
    if role == Administrador:
        return True
    
    return LivroUsuario.objects.filter(livro=avaliacao.livro, autor=user).exists()
