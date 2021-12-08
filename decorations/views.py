import json
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min
from mainapp.views import addPurchasesViewed, productRecommendation
from decorations.models import Decoration, AgencyDecoration, ImageLibrary, Reviews, Questions, Audits, AuditElement
# Create your views here.

def decorationsView(request):
    agencies = AgencyDecoration.objects.all()[:20]
    agencies_count = AgencyDecoration.objects.all().count()
    for agency in agencies:
        agency.additional_data = Decoration.objects.filter(agency=agency)[:4]
    return render(request, 'decorations.html', {"agencies": agencies, "agencies_count": agencies_count})

def decorationView(request, decoration_slug):
    subcategories = []
    agency = get_object_or_404(AgencyDecoration, slug=decoration_slug)
    decorations = Decoration.objects.filter(agency=agency)
    audit = Audits.objects.filter(agency_id=agency.id)[:2]
    reviews = Reviews.objects.filter(agency_id=agency.id)[:2]
    questions = Questions.objects.filter(agency_id=agency.id)[:2]
    recommendations = productRecommendation()
    
    if not request.session.get('viewed_products'):
        request.session['viewed_products'] = list()
        listPurchasesViewed = False
    else:
       listPurchasesViewed = request.session['viewed_products']
    
    for decoration in decorations:
        if not decoration.subcategory in subcategories:
            subcategories.append(decoration.subcategory)

    if not audit:
        audit_elements = False
    else:
        audit_elements = AuditElement.objects.filter(audit_id=audit[0].id)[:2]

    if not questions:
        questions = False

    if not reviews:
        reviews = False
        
    return render(request, 'decoration.html', {
        "agency": agency,
        "decorations": decorations,
        "name": "decoration",
        "subcategories": subcategories,
        'audit_elements': audit_elements,
        'reviews': reviews,
        'questions': questions,
        'recommendations': recommendations,
        'listPurchasesViewed': listPurchasesViewed
    })