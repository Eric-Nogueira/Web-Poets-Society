from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from avaliacao.forms import AvaliacaoForm
from avaliacao.models import Avaliacao
from rolepermissions.checkers import has_permission, has_object_permission

from livro_usuario.models import Livro_Usuario

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

    if request.method == 'POST':
        user = request.user

        tem_permissao_qualquer = user.has_perm('avaliacao.editar_qualquer_avaliacao')
        
        # Navegação UML: Avaliacao -> Livro -> LivroUsuario
        e_autor_do_livro = Livro_Usuario.objects.filter(livro=avaliacao.livro, autor=user).exists()
        
        tem_permissao_proprio = user.has_perm('avaliacao.editar_proprio_avaliacao') and e_autor_do_livro

        if not (tem_permissao_qualquer or tem_permissao_proprio):
            messages.error(request, "Você não tem permissão para editar esta avaliação.")
            return redirect('home')
        
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

    if request.method == 'POST':
        user = request.user
        
        tem_permissao_qualquer = user.has_perm('avaliacao.excluir_qualquer_avaliacao')
                
                # Navegação UML: Avaliacao -> Livro -> LivroUsuario
        e_autor_do_livro = Livro_Usuario.objects.filter(livro=avaliacao.livro, autor=user).exists()
                
        tem_permissao_proprio = user.has_perm('avaliacao.excluir_proprio_avaliacao') and e_autor_do_livro
        
        if not (tem_permissao_qualquer or tem_permissao_proprio):
                    messages.error(request, "Você não tem permissão para excluir esta avaliação.")
                    return redirect('home')
                
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