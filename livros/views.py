from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from livro_colecao.models import Livro_Colecao
from livro_usuario.models import Livro_Usuario

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
