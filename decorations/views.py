import json
from django.shortcuts import render
from decorations.models import Decoration, AgencyDecoration
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min
# Create your views here.

def decorationsView(request):
    agencies = AgencyDecoration.objects.all()[:20]
    agencies_count = AgencyDecoration.objects.all().count()
    return render(request, 'decorations.html', {"agencies": agencies, "agencies_count": agencies_count})

def decorationView(request, decoration_slug):
    subcategories = []
    agency = get_object_or_404(AgencyDecoration, slug=decoration_slug)
    decorations = Decoration.objects.filter(agency=agency)
    for decoration in decorations:
        if not decoration.subcategory in subcategories:
            subcategories.append(decoration.subcategory)
    return render(request, 'decoration.html', {
        "agency": agency,
        "decorations": decorations,
        "name": "decoration",
        "subcategories": subcategories
    })