from django.shortcuts import render
from .models import Kategori, GaleriItem


# Create your views here.
def index(request):
    galeri_items = GaleriItem.objects.all()
    context = {
        "galeri_items": galeri_items
    }
    return render(request, 'kcrgaleri/index.html', context)