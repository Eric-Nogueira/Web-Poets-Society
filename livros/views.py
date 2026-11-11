from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from livro_colecao.models import Livro_Colecao
from livro_usuario.models import Livro_Usuario

from usuario.models import Usuario
from colecao.models import Colecao

from .forms import LivroForm
from .models import Livro


@login_required
def lista_livros(request):
    """Lista dos livros cadastrados.

    Varios botoes do site diziam "Ver livros cadastrados" mas levavam para o
    formulario de cadastro; agora existe a pagina de verdade.
    """
    livros = Livro.objects.order_by('titulo').prefetch_related(
        'livro_usuario_set__autor',
        'livro_colecao_set__colecao',
    )
    return render(request, 'view/livros.html', {'livros': livros})


@login_required
def criar_livro(request):
    """Mostra o formulario de cadastro de Livro e salva quando enviado."""
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save()

            # Liga o livro a cada autor selecionado (tabela Livro_Usuario).
            for autor in form.cleaned_data['autores']:
                Livro_Usuario.objects.create(livro=livro, autor=autor)

            # Liga o livro a colecao escolhida, se houver (tabela Livro_Colecao).
            colecao = form.cleaned_data['colecao']
            if colecao:
                Livro_Colecao.objects.create(livro=livro, colecao=colecao)

            messages.success(request, f'Livro "{livro.titulo}" cadastrado com sucesso!')
            return redirect('livros:criar')
    else:
        form = LivroForm()

    return render(request, 'form/livro_form.html', {'form': form})

@login_required
def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        
        user = request.user

    # 1. O usuário tem a permissão global? (Ex: Administrador)
    tem_permissao_qualquer = user.has_perm('livros.editar_qualquer_livro')
    
    # 2. O usuário tem a permissão de próprio E é o autor do livro?
    # Verificamos na tabela LivroUsuario que está no seu UML
    e_autor = Livro_Usuario.objects.filter(livro=livro, autor=user).exists()
    tem_permissao_proprio = user.has_perm('livros.editar_proprio_livro') and e_autor

    if not (tem_permissao_qualquer or tem_permissao_proprio):
        messages.error(request, "Você não tem permissão para editar este livro.")
        # Mude 'livros:lista' para o nome real da URL para onde ele deve voltar
        return redirect('livros:lista') 
    
        form = LivroForm(request.POST, instance=livro)

        if form.is_valid():
            form.save()

            # Atualiza os autores
            Livro_Usuario.objects.filter(livro=livro).delete()

            for autor in form.cleaned_data['autores']:
                Livro_Usuario.objects.create(
                    livro=livro,
                    autor=autor
                )

            # Atualiza a coleção
            Livro_Colecao.objects.filter(livro=livro).delete()

            colecao = form.cleaned_data['colecao']

            if colecao:
                Livro_Colecao.objects.create(
                    livro=livro,
                    colecao=colecao
                )

            messages.success(
                request,
                f'Livro "{livro.titulo}" atualizado com sucesso!'
            )

            return redirect('livros:lista')

    else:
        autores = Usuario.objects.filter(
            livro_usuario__livro=livro
        )

        colecao = Colecao.objects.filter(
            livro_colecao__livro=livro
        ).first()

        form = LivroForm(
            instance=livro,
            initial={
                'autores': autores,
                'colecao': colecao
            }
        )

    return render(
        request,
        'form/editar_livro.html',
        {
            'form': form,
            'livro': livro
        }
    )


@login_required
def deletar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    
    if request.method == 'POST':
        
        user = request.user

    # 1. O usuário tem a permissão global? (Ex: Administrador)
    tem_permissao_qualquer = user.has_perm('livros.excluir_qualquer_livro')
    
    # 2. O usuário tem a permissão de próprio E é o autor do livro?
    # Verificamos na tabela LivroUsuario que está no seu UML
    e_autor = Livro_Usuario.objects.filter(livro=livro, autor=user).exists()
    tem_permissao_proprio = user.has_perm('livros.excluir_proprio_livro') and e_autor

    if not (tem_permissao_qualquer or tem_permissao_proprio):
        messages.error(request, "Você não tem permissão para excluir este livro.")
        # Mude 'livros:lista' para o nome real da URL para onde ele deve voltar
        return redirect('livros:lista') 

        return render(
            request,
            'form/deletar_livro.html',
            {
                'livro': livro
            }
        )