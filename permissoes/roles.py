from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'excluir_qualquer_editora': True,
        'excluir_qualquer_usuario': True,
        'excluir_proprio_editora': True,
        'excluir_proprio_usuario': True,
        'editar_proprio_livro': True,
        'editar_qualquer_livro': True,
        'excluir_proprio_livro': True,
        'excluir_qualquer_livro': True,
        'editar_proprio_edicao': True,
        'editar_qualquer_edicao': True,
        'excluir_proprio_edicao': True,
        'excluir_qualquer_edicao': True,
        'editar_proprio_capitulo': True,
        'editar_qualquer_capitulo': True,
        'excluir_proprio_capitulo': True,
        'excluir_qualquer_capitulo': True,
        'editar_proprio_colecao': True,
        'editar_qualquer_colecao': True,
        'excluir_proprio_colecao': True,
        'excluir_qualquer_colecao': True,
        'editar_proprio_avaliacao': True,
        'editar_qualquer_avaliacao': True,
        'excluir_proprio_avaliacao': True,
        'excluir_qualquer_avaliacao': True
    }
    
class Usuario(AbstractUserRole):
    available_permissions = {
        'excluir_proprio_editora': True,
        'excluir_proprio_usuario': True,
        'editar_proprio_livro': True,
        'excluir_proprio_livro': True,
        'editar_proprio_edicao': True,
        'excluir_proprio_edicao': True,
        'editar_proprio_capitulo': True,
        'excluir_proprio_capitulo': True,
        'editar_proprio_colecao': True,
        'excluir_proprio_colecao': True,
        'editar_proprio_avaliacao': True,
        'excluir_proprio_avaliacao': True
    }
    
