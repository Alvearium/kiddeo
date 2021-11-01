from django.shortcuts import render

# Create your views here.
def foodsView(request):
    return render(request, 'foods.html', {})