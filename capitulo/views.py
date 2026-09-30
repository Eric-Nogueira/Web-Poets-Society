from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from livros.models import Livro
from .models import Capitulo
from .forms import CapituloForm


@login_required
def criar_capitulo(request):
    """Mostra o formulario de cadastro de Capitulo e salva quando enviado."""
    if request.method == 'POST':
        form = CapituloForm(request.POST)
        if form.is_valid():
            capitulo = form.save()
            messages.success(request, f'Capitulo "{capitulo.titulo}" cadastrado com sucesso!')
            return redirect('capitulo:criar')
    else:
        form = CapituloForm()

    return render(request, 'form/capitulo_form.html', {'form': form})

@login_required
def lista_capitulos(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    capitulos = Capitulo.objects.filter(
        livro=livro
    ).order_by('id')

    return render(
        request,
        'view/capitulos.html',
        {
            'livro': livro,
            'capitulos': capitulos,
        }
    )

@login_required
def editar_capitulo(request, capitulo_id):
    capitulo = get_object_or_404(
        Capitulo,
        id=capitulo_id
    )

    if request.method == 'POST':
        form = CapituloForm(
            request.POST,
            instance=capitulo
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                f'Capítulo "{capitulo.titulo}" atualizado com sucesso!'
            )

            return redirect(
                'capitulo:lista',
                livro_id=capitulo.livro.id
            )

    else:
        form = CapituloForm(
            instance=capitulo
        )

    return render(
        request,
        'form/editar_capitulo.html',
        {
            'form': form,
            'capitulo': capitulo
        }
    )


@login_required
def deletar_capitulo(request, capitulo_id):
    capitulo = get_object_or_404(
        Capitulo,
        id=capitulo_id
    )

    livro_id = capitulo.livro.id

    if request.method == 'POST':
        capitulo.delete()

        messages.success(
            request,
            'Capítulo deletado com sucesso!'
        )

        return redirect(
            'capitulo:lista',
            livro_id=livro_id
        )

    return render(
        request,
        'form/deletar_capitulo.html',
        {
            'capitulo': capitulo
        }
    )