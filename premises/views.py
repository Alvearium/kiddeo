import json
from itertools import chain
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.db.models import Min
from mainapp.views import addPurchasesViewed, productRecommendation
from django.shortcuts import get_object_or_404, get_list_or_404
from premises.models import Premises, ImageLibrary, Reviews, Questions, Audits, AuditElement

# Create your views here.
def premisesView(request):
    premises = Premises.objects.all()[:7]
    premises_count = Premises.objects.all().count()
    return render(request, 'premises.html', {"premises": premises, "premises_count": premises_count})

def premiseView(request, premise_slug):
    premise = get_object_or_404(Premises, slug=premise_slug)
    min_price_dict = Premises.objects.all().aggregate(Min('price'))
    min_price = min_price_dict['price__min']
    cheaper = get_object_or_404(Premises, price=min_price)
    audit = Audits.objects.filter(premise_id=premise.id)[:2]
    reviews = Reviews.objects.filter(premise_id=premise.id)[:2]
    questions = Questions.objects.filter(premise_id=premise.id)[:2]
    recommendations = productRecommendation()
    listPurchasesViewed = addPurchasesViewed(request, premise, 'premise')
    district_list = get_list_or_404(Premises, district = premise.district)

    if not audit:
        audit_elements = False
    else:
        audit_elements = AuditElement.objects.filter(audit_id=audit[0].id)[:2]

    if not questions:
        questions = False

    if not reviews:
        reviews = False

    return render(request, 'premise.html', {
        "premise": premise,
        'name':'Premises',
        'min_price': min_price,
        'cheaper_slug': cheaper.slug,
        'audit_elements': audit_elements,
        'reviews': reviews,
        'questions': questions,
        'district_list': district_list,
        'recommendations': recommendations,
        'listPurchasesViewed': listPurchasesViewed
    })
