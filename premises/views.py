import json
from django.shortcuts import render
from premises.models import Premises, PremisesImage, Audits, AuditElement
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min

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

    audit = Audits.objects.filter(premise_id=premise.id)

    if not audit:
        audit_elements = False
    else:
        audit_elements = AuditElement.objects.filter(audit_id=audit[0].id)

    return render(request, 'premise.html', {
        "premise": premise,
        'min_price': min_price,
        'cheaper_slug': cheaper.slug,
        'audit_elements': audit_elements
    })