import json
from itertools import chain
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.db.models import Min
from mainapp.views import addPurchasesViewed, productRecommendation
from django.shortcuts import get_object_or_404, get_list_or_404
from holidays.models import Holidays, ImageLibrary, Reviews, Questions, Audits, AuditElement

# Create your views here.
def holidaysView(request):
    holidays = Holidays.objects.all()[:7]
    holidays_count = Holidays.objects.all().count()
    return render(request, 'holidays.html', {"holidays": holidays, "holidays_count": holidays_count})

def holidayView(request, holiday_slug):
    holiday = get_object_or_404(Holidays, slug=holiday_slug)
    min_price_dict = Holidays.objects.all().aggregate(Min('price'))
    min_price = min_price_dict['price__min']
    cheaper = get_object_or_404(Holidays, price=min_price)
    audit = Audits.objects.filter(holiday_id=holiday.id)[:2]
    reviews = Reviews.objects.filter(holiday_id=holiday.id)[:2]
    questions = Questions.objects.filter(holiday_id=holiday.id)[:2]
    recommendations = productRecommendation()
    listPurchasesViewed = addPurchasesViewed(request, holiday, 'holiday')
    district_list = get_list_or_404(Holidays, district = holiday.district)

    if not audit:
        audit_elements = False
    else:
        audit_elements = AuditElement.objects.filter(audit_id=audit[0].id)[:2]

    if not questions:
        questions = False

    if not reviews:
        reviews = False

    return render(request, 'holiday.html', {
        "holiday": holiday,
        'name':'Holidays',
        'min_price': min_price,
        'cheaper_slug': cheaper.slug,
        'audit_elements': audit_elements,
        'reviews': reviews,
        'questions': questions,
        'district_list': district_list,
        'recommendations': recommendations,
        'listPurchasesViewed': listPurchasesViewed
    })
