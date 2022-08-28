from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
# Create your views here.


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def novo_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'formprodutos.html', {'form': form})

def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    
    return render(request, 'formprodutos.html', {'form': form, 'produto': produto})


def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    
    return render(request, 'confirmacaodelete.html', {'produto': produto})