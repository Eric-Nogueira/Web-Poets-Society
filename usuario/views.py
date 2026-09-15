from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from capitulo.models import Capitulo
from edicao.models import Edicao
from editora.models import Editora
from livros.models import Livro

from .forms import UsuarioForm
from .models import Usuario


@login_required
def home(request):
    context = {
        'editoras_recentes': Editora.objects.select_related('resposavel').order_by('-id')[:10],
        'usuarios_recentes': Usuario.objects.order_by('-date_joined')[:10],
        'edicoes_recentes': Edicao.objects.select_related('editora', 'livro').order_by('-id')[:10],
    }

    return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UsuarioForm()
    return render(request, 'form/register.html', {'form': form})


def _dados_do_perfil(usuario):
    """Monta os numeros e a lista de livros de um Usuario.

    Usado tanto pelo perfil do proprio usuario quanto pelo perfil publico,
    para os dois nao sairem do ar com contas diferentes.
    """
    if usuario is None:
        return {
            'livros_info': [],
            'livros_count': 0,
            'capitulos_count': 0,
            'colecoes_count': 0,
        }

    livros = (
        Livro.objects
        .filter(livro_usuario__autor=usuario)
        .distinct()
        .order_by('titulo')
    )

    livros_info = []
    colecoes_vistas = set()
    for livro in livros:
        colecoes = [lc.colecao for lc in livro.livro_colecao_set.all()]
        for c in colecoes:
            colecoes_vistas.add(c.id)
        livros_info.append({
            'livro': livro,
            'capitulos_count': livro.capitulo_set.count(),
            'colecoes': colecoes,
        })

    return {
        'livros_info': livros_info,
        'livros_count': livros.count(),
        'capitulos_count': Capitulo.objects.filter(livro__in=livros).count(),
        'colecoes_count': len(colecoes_vistas),
    }


@login_required
def perfil(request):
    """Perfil do usuario logado, com os livros que ele assina como autor."""
    # Nem todo request.user tem uma linha em Usuario (ex: superuser criado
    # via createsuperuser nao passa pelo formulario de cadastro).
    usuario = Usuario.objects.filter(pk=request.user.pk).first()

    context = _dados_do_perfil(usuario)
    context['usuario'] = usuario
    context['conta'] = usuario or request.user

    return render(request, 'view/profile.html', context)


@login_required
def perfil_publico(request, username):
    """Perfil de OUTRO usuario, somente leitura."""
    usuario = get_object_or_404(Usuario, username=username)

    context = _dados_do_perfil(usuario)
    context['usuario'] = usuario
    context['conta'] = usuario
    context['e_meu_perfil'] = usuario.pk == request.user.pk

    return render(request, 'view/perfil-publico.html', context)
