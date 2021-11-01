from django.shortcuts import render

# Create your views here.
def premisesView(request):
    return render(request, 'premises.html', {})