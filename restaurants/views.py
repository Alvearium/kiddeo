from django.shortcuts import render

# Create your views here.
def foodsView(request):
    return render(request, 'foods.html', {})

def foodView(request):
    return render(request, 'food.html', {})