import json
from django.shortcuts import render
from animators.models import Agency, Animator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min

# Create your views here.
def animatorsView(request):
    agencies = Agency.objects.all()[:20]
    agencies_count = Agency.objects.all().count()
    return render(request, 'animators.html', {"agencies": agencies, "agencies_count": agencies_count})

def animatorView(request, animator_slug):
    subcategories = []
    agency = get_object_or_404(Agency, slug=animator_slug)
    animators = Animator.objects.filter(agency=agency)
    for animator in animators:
        if not animator.subcategory in subcategories:
            subcategories.append(animator.subcategory)
    return render(request, 'animator.html', {
        "agency": agency,
        "animators": animators,
        "name": "animator",
        "subcategories": subcategories
    })