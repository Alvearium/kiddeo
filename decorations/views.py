from django.shortcuts import render

# Create your views here.

def decorationsView(request):
    return render(request, 'decorations.html', {})