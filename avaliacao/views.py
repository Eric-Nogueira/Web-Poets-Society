from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from avaliacao.forms import AvaliacaoForm
from avaliacao.models import Avaliacao
from rolepermissions.checkers import has_permission, has_object_permission

@login_required
def register_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, request.FILES)
        if form.is_valid():
            avaliacao = form.save()
            messages.success(request, f'Avaliacao "{avaliacao.nota}" cadastrada com sucesso!')
            return redirect('home')
    else:
        form = AvaliacaoForm()
    return render(request, 'form/register_avaliacao.html', {'form': form})

@login_required
def lista_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all().order_by('-data_avaliacao')

    return render(request, 'view/avaliacoes.html', {'avaliacoes': avaliacoes})

@login_required
def curtir_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)

    if request.user in avaliacao.curtida.all():
        avaliacao.curtida.remove(request.user)
    else:
        avaliacao.curtida.add(request.user)

    return redirect('avaliacao:lista')

@login_required
def editar_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(
        Avaliacao,
        id=avaliacao_id
    )
    user = request.user

    if request.method == 'POST':
        if has_permission(user, 'editar_qualquer_avaliacao'):
            pass
        elif has_permission(user, 'editar_proprio_avaliacao') and has_object_permission('gerenciar_avaliacao', user, avaliacao):
            pass
        else:
            messages.error(request, 'Você não tem permissão para editar essa avaliação.')
            return redirect('livros:lista')
        form = AvaliacaoForm(
            request.POST,
            instance=avaliacao
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Avaliação atualizada com sucesso!'
            )

            return redirect('avaliacao:lista')

    else:
        form = AvaliacaoForm(
            instance=avaliacao
        )

    return render(
        request,
        'form/editar_avaliacao.html',
        {
            'form': form,
            'avaliacao': avaliacao
        }
    )


@login_required
def deletar_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(
        Avaliacao,
        id=avaliacao_id
    )
    user = request.user

    if request.method == 'POST':
        if has_permission(user, 'excluir_qualquer_avaliacao'):
            pass
        elif has_permission(user, 'excluir_proprio_avaliacao') and has_object_permission('gerenciar_colecao', user, avaliacao):
            pass
        else:
            messages.error(request, 'Você não tem permissão para excluir essa avaliação.')
            return redirect('livros:lista')
        avaliacao.delete()

        messages.success(
            request,
            'Avaliação deletada com sucesso!'
        )

        return redirect('avaliacao:lista')

    return render(
        request,
        'form/deletar_avaliacao.html',
        {
            'avaliacao': avaliacao
        }
    )