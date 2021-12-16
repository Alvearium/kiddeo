import json
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min
from mainapp.views import addPurchasesViewed, productRecommendation
from photos.models import AgencyPhotos, Services, ImageLibrary, Reviews, Questions, Audits, AuditElement

# Create your views here.
def photosView(request):
    agencies = AgencyPhotos.objects.all()[:7]
    agencies_count = AgencyPhotos.objects.all().count()
    
    for agency in agencies:
        agency.additional_data = Services.objects.filter(agency=agency)[:4]

    return render(request, 'photos.html', {"agencies": agencies, "agencies_count": agencies_count})

def serviceView(request, service_slug):
    subcategories = []
    agency = get_object_or_404(AgencyPhotos, slug=service_slug)
    services = Services.objects.filter(agency=agency)
    audit = Audits.objects.filter(agency_id=agency.id)[:2]
    reviews = Reviews.objects.filter(agency_id=agency.id)[:2]
    questions = Questions.objects.filter(agency_id=agency.id)[:2]
    recommendations = productRecommendation()
    
    if not request.session.get('viewed_products'):
        request.session['viewed_products'] = list()
        listPurchasesViewed = False
    else:
       listPurchasesViewed = request.session['viewed_products']
       
    for service in services:
        if not service.subcategory in subcategories:
            subcategories.append(service.subcategory)

    if not audit:
        audit_elements = False
    else:
        audit_elements = AuditElement.objects.filter(audit_id=audit[0].id)[:2]

    if not questions:
        questions = False

    if not reviews:
        reviews = False
        
    return render(request, 'service.html', {
        "agency": agency,
        "services": services,
        "name": "services",
        "subcategories": subcategories,
        'audit_elements': audit_elements,
        'reviews': reviews,
        'questions': questions,
        'recommendations': recommendations,
        'listPurchasesViewed': listPurchasesViewed
    })