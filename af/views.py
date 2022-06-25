from django.shortcuts import render
from .models import HomeCarousel, Product, JumiaCarousel, JumiaProduct



def home(request):
    carou = HomeCarousel.objects.all()
    proc = Product.objects.all()

    context = {
        'carou' : carou,
        'proc': proc,

    }
    return render(request, 'af/amazon.html', context)


def jumia(request):
    carou = JumiaCarousel.objects.all()
    proc = JumiaProduct.objects.all()

    context = {
        'carou' : carou,
        'proc': proc,
        'navbar': 'jumia'
    }
    return render(request, 'af/jumia.html', context)
def about(request):
    return render(request, 'af/about.html')

