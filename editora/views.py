from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import EditoraForm


@login_required
def register_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            editora = form.save()
            messages.success(request, f'Editora "{editora}" cadastrada com sucesso!')
            return redirect('home')
    else:
        form = EditoraForm()
    return render(request, 'form/register_editora.html', {'form': form})
