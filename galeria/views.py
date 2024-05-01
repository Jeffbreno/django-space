from django.shortcuts import render, get_object_or_404
from galeria.models import FotoGrafia


def index(request):
    fotografias = FotoGrafia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(FotoGrafia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    fotografias = FotoGrafia.objects.order_by("data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_busca = request.GET["buscar"]
        if nome_a_busca:
            fotografias = fotografias.filter(nome__icontains=nome_a_busca)

    return render(request, "galeria/buscar.html", {"cards": fotografias})
