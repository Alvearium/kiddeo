import json
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min
from mainapp.views import addPurchasesViewed, productRecommendation
from animators.models import Agency, Animator, ImageLibrary, Reviews, Questions, Audits, AuditElement

# Create your views here.
def animatorsView(request):
    agencies = Agency.objects.all()[:20]
    agencies_count = Agency.objects.all().count()
    for agency in agencies:
        agency.additional_data = Animator.objects.filter(agency=agency)[:4]


    return render(request, 'animators.html', {"agencies": agencies, "agencies_count": agencies_count})

def animatorView(request, animator_slug):
    subcategories = []
    agency = get_object_or_404(Agency, slug=animator_slug)
    animators = Animator.objects.filter(agency=agency)
    audit = Audits.objects.filter(agency_id=agency.id)[:2]
    reviews = Reviews.objects.filter(agency_id=agency.id)[:2]
    questions = Questions.objects.filter(agency_id=agency.id)[:2]
    recommendations = productRecommendation()
    for animator in animators:
        if not animator.subcategory in subcategories:
            subcategories.append(animator.subcategory)

    if not audit:
        audit_elements = False
    else:
        audit_elements = AuditElement.objects.filter(audit_id=audit[0].id)[:2]

    if not questions:
        questions = False

    if not reviews:
        reviews = False

    return render(request, 'animator.html', {
        "agency": agency,
        "animators": animators,
        "name": "animator",
        "subcategories": subcategories,
        'audit_elements': audit_elements,
        'reviews': reviews,
        'questions': questions,
        'recommendations': recommendations,
    })