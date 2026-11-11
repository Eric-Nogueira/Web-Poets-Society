from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from livro_usuario.models import Livro_Usuario

from .forms import EdicaoForm
from .models import Edicao

from rolepermissions.checkers import has_permission, has_object_permission

@login_required
def register_edicao(request):
    if request.method == 'POST':
        form = EdicaoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            edicao = form.save()

            messages.success(
                request,
                f'Edicao "{edicao.titulo}" cadastrada com sucesso!'
            )

            return redirect('home')
    else:
        form = EdicaoForm()

    return render(
        request,
        'form/register_edicao.html',
        {'form': form}
    )


@login_required
def editar_edicao(request, edicao_id):
    edicao = get_object_or_404(Edicao, id=edicao_id)
    user = request.user

    tem_permissao_qualquer = user.has_perm('edicao.editar_qualquer_edicao')
    
    # Navegação UML: Edicao -> Livro -> LivroUsuario OU Edicao -> Editora -> responsavel
    e_autor_do_livro = Livro_Usuario.objects.filter(livro=edicao.livro, autor=user).exists()
    e_responsavel_editora = edicao.editora and edicao.editora.responsavel == user
    
    tem_permissao_proprio = user.has_perm('edicao.editar_proprio_edicao') and (e_autor_do_livro or e_responsavel_editora)

    if not (tem_permissao_qualquer or tem_permissao_proprio):
        messages.error(request, "Você não tem permissão para editar esta edição.")
        return redirect('home') # Ajuste para a URL correta
    
    
    if request.method == 'POST':
        form = EdicaoForm(
            request.POST,
            request.FILES,
            instance=edicao
        )

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EdicaoForm(instance=edicao)

    return render(
        request,
        'form/editar_edicao.html',
        {
            'form': form,
            'edicao': edicao
        }
    )


@login_required
def deletar_edicao(request, edicao_id):
    edicao = get_object_or_404(Edicao, id=edicao_id)
    
    if request.method == 'POST': 
        user = request.user
        
        tem_permissao_qualquer = user.has_perm('edicao.excluir_qualquer_edicao')
            
            # Navegação UML: Edicao -> Livro -> LivroUsuario OU Edicao -> Editora -> responsavel
        e_autor_do_livro = Livro_Usuario.objects.filter(livro=edicao.livro, autor=user).exists()
        e_responsavel_editora = edicao.editora and edicao.editora.responsavel == user
            
        tem_permissao_proprio = user.has_perm('edicao.excluir_proprio_edicao') and (e_autor_do_livro or e_responsavel_editora)
        
        if not (tem_permissao_qualquer or tem_permissao_proprio):
                messages.error(request, "Você não tem permissão para deletar esta edição.")
                return redirect('home')     
        edicao.delete()

    return render(
        request,
        'form/deletar_edicao.html',
        {
            'edicao': edicao
        }
    )