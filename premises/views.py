import json
from itertools import chain
from mainapp.cart import Cart
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.db.models import Min
from mainapp.views import addPurchasesViewed
from django.shortcuts import get_object_or_404, get_list_or_404
from premises.models import Premises, PremisesImage, Audits, AuditElement
from animators.models import Agency, Animator
from restaurants.models import Restaurant, Food
from decorations.models import AgencyDecoration, Decoration

# Create your views here.
def premisesView(request):
    premises = Premises.objects.all()[:20]
    premises_count = Premises.objects.all().count()
    return render(request, 'premises.html', {"premises": premises, "premises_count": premises_count})

def premiseView(request, premise_slug):
    premise = get_object_or_404(Premises, slug=premise_slug)
    min_price_dict = Premises.objects.all().aggregate(Min('price'))
    min_price = min_price_dict['price__min']
    cheaper = get_object_or_404(Premises, price=min_price)
    recommendations = productRecommendation()
    audit = Audits.objects.filter(premise_id=premise.id)
    listPurchasesViewed = addPurchasesViewed(request, premise, 'premise')
    district_list = get_list_or_404(Premises, district = premise.district)

    if not audit:
        audit_elements = False
    else:
        audit_elements = AuditElement.objects.filter(audit_id=audit[0].id)

    return render(request, 'premise.html', {
        "premise": premise,
        'min_price': min_price,
        'cheaper_slug': cheaper.slug,
        'audit_elements': audit_elements,
        'district_list': district_list,
        'recommendations': recommendations,
        'listPurchasesViewed': listPurchasesViewed
    })

def productRecommendation():

    result_list = []

    result_list.append(Premises.objects.order_by('?').first())
    result_list.append(Food.objects.order_by('?').first())
    result_list.append(AgencyDecoration.objects.order_by('?').first())
    result_list.append(Agency.objects.order_by('?').first())

    return(result_list)



# print(request.session['cart'])
