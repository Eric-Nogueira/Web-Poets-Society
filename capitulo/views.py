from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from livros.models import Livro
from .models import Capitulo
from .forms import CapituloForm
from rolepermissions.checkers import has_permission, has_object_permission


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
    user = request.user

    if request.method == 'POST':
        if has_permission(user, 'editar_qualquer_capitulo'):
            pass
        
        elif has_permission(user, 'editar_qualquer_capitulo') and has_object_permission('gerenciar_capitulo', user, capitulo):
            pass
        else:
            messages.error(request, 'Você não tem permissão para editar esse capítulo.')
            return redirect('livros:lista')
            
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
    user = request.user

    livro_id = capitulo.livro.id

    if request.method == 'POST':
        if has_permission(user, 'excluir_qualquer_capitulo'):
            pass
        
        elif has_permission(user, 'excluir_proprio_capitulo') and has_object_permission('gerenciar_capitulo', user, capitulo):
            pass
        else:
            messages.error(request, 'Você não tem permissão para excluir esse capítulo.')
            return redirect('livros:lista')
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