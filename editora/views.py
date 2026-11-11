from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import EditoraForm
from .models import Editora

from rolepermissions.checkers import has_object_permission, has_permission


@login_required
def register_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)

        if form.is_valid():
            editora = form.save()
            messages.success(
                request,
                f'Editora "{editora}" cadastrada com sucesso!'
            )
            return redirect('home')
    else:
        form = EditoraForm()

    return render(
        request,
        'form/register_editora.html',
        {'form': form}
    )


@login_required
def editar_editora(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)

    if request.method == 'POST':
        user = request.user

        tem_permissao_qualquer = user.has_perm('editora.editar_qualquer_editora')
    
    # Navegação UML: Editora -> responsavel
        e_responsavel = editora.responsavel == user
    
        tem_permissao_proprio = user.has_perm('editora.editar_proprio_editora') and e_responsavel

        if not (tem_permissao_qualquer or tem_permissao_proprio):
            messages.error(request, "Você não é o responsável por esta editora e não pode editá-la.")
            return redirect('home')
        form = EditoraForm(
            request.POST,
            instance=editora
        )

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditoraForm(instance=editora)

    return render(
        request,
        'form/editar_editora.html',
        {
            'form': form,
            'editora': editora
        }
    )


@login_required
def deletar_editora(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)

    if request.method == 'POST':
        user = request.user
        
        tem_permissao_qualquer = user.has_perm('editora.excluir_qualquer_editora')
            
            # Navegação UML: Editora -> responsavel
        e_responsavel = editora.responsavel == user
            
        tem_permissao_proprio = user.has_perm('editora.excluir_proprio_editora') and e_responsavel
        
        if not (tem_permissao_qualquer or tem_permissao_proprio):
                    messages.error(request, "Você não é o responsável por esta editora e não pode excluí-la.")
                    return redirect('home')
        editora.delete()
        return redirect('home')

    return render(
        request,
        'form/deletar_editora.html',
        {
            'editora': editora
        }
    )