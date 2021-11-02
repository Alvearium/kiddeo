from django.shortcuts import render

# Create your views here.
def animatorsView(request):
    return render(request, 'animators.html', {})

def animatorView(request):
    return render(request, 'animator.html', {})