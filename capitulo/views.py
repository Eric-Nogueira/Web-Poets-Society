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
