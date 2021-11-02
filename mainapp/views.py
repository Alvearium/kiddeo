from django.shortcuts import render


# Create your views here.
def indexView(request):
    return render(request, 'index.html', {})

def cartView(request):
    return render(request, 'cart.html', {})