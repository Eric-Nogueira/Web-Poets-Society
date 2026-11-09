# livros/permissions.py
from rolepermissions.permissions import register_object_checker
from permissoes.roles import Editor
from .models import LivroUsuario

@register_object_checker()
def gerenciar_edicao(role, user, edicao):
    # 1. Se for um Editor global, pode tudo
    if role == Editor:
        return True
    
    # 2. É o autor do livro ao qual esta edição pertence?
    e_autor_do_livro = LivroUsuario.objects.filter(livro=edicao.livro, autor=user).exists()
    if e_autor_do_livro:
        return True
        
    # 3. É o responsável pela Editora que publicou esta edição?
    # (Verificando a ligação Edicao -> Editora -> responsavel do seu UML)
    if edicao.editora and edicao.editora.responsavel == user:
        return True
        
    return False