from django.shortcuts import redirect, render, get_object_or_404
from apps.galeria.forms import FotografiaForms
from apps.galeria.models import Fotografia
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Realize o login para acessar o conteúdo")
        return redirect('login')
        
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Realize o login para acessar o conteúdo")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains= nome_a_buscar)
    
    return render(request, 'galeria/index.html', {"cards" : fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Realize o login para acessar o conteúdo")
        return redirect('login')
    
    form = FotografiaForms
    
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem cadastrada com sucesso!')
            return redirect('index')
    return render(request, 'galeria/nova_imagem.html', {'form' : form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia) # O que nao for mudado ele pega do que ja existia (explicando o instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso!')
            return redirect('index')
    
    return render(request, 'galeria/editar_imagem.html', {'form' : form, 'foto_id' : foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id = foto_id)
    fotografia.delete()
    messages.success(request, 'Imagem removida com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {'cards': fotografias})