from itertools import chain
from django.shortcuts import redirect, render
from animators.models import Agency
from decorations.models import AgencyDecoration
from mainapp.views import addPurchasesViewed
from premises.models import Premises, PremisesImage
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Min

from restaurants.models import Food

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
    district_list = get_list_or_404(Premises, district = premise.district)
    recomendations = productRecomendation()
    premises_images = PremisesImage.objects.filter(premises_id=premise.id)
    listPurchasesViewed = addPurchasesViewed(request, premise, 'premise')
    print(listPurchasesViewed)
    return render(request, 'premise.html', {
        "premise": premise,
        'min_price': min_price,
        'cheaper_slug': cheaper.slug,
        'premises_images': premises_images,
        'district_list': district_list,
        'recomendations': recomendations,
        'listPurchasesViewed': listPurchasesViewed,
    })

def SplitStringAndFilteringWithoutOrder(string):
    if ',' in string:
        array = dict(e.split('=') for e in string.split(','))
        premises = Premises.objects.filter(**array)
        count = Premises.objects.filter(**array).count()
    else:
        array = string.split('=')
        premises = Premises.objects.filter(array)
        count = Premises.objects.filter(array).count()
    return [premises, count]

def SplitStringAndFilteringWithOrder(string, order_by):
    if ',' in string:
        array = dict(e.split('=') for e in string.split(','))
        premises = Premises.objects.filter(**array).order_by(order_by)
        count = Premises.objects.filter(**array).count()
    else:
        array = string.split('=')
        premises = Premises.objects.filter(array).order_by(order_by)
        count = Premises.objects.filter(array).count()
    return [premises, count]

def premisesSidebarFilters(request):
    result = ''
    filters = request.POST.get('filters', None)
    order_by = request.POST.get('order_by', None)
    if filters != None and order_by != None:
       func_data = SplitStringAndFilteringWithOrder(filters, order_by)
       premises = func_data[0]
       count = func_data[1]
    elif filters != None and order_by == None:
       func_data = SplitStringAndFilteringWithoutOrder(filters)
       premises = func_data[0]
       count = func_data[1]
    else:
       premises = Premises.objects.all().order_by(order_by)
       count = Premises.objects.all().count()

    for premise in premises:
        result += premise.title + '<div class="premises-card"><div class="wrap-thumbnail"><div class="discount"><h4>Подарок</h4></div><div class="tap"><i class="fas fa-hand-pointer"></i></div><div class="camera"><i class="fas fa-video"></i></div><img src="https://imgholder.ru/1920x1080/8493a8/adb9ca&text=IMAGE+HOLDER&font=kelson" alt="Image"> <div class="blackout"></div></div><div class="premises-card-content"></div></div>'
    responseData  = {
        'objects': result,
        'count': count
    }

    return JsonResponse(responseData)

def productRecomendation():

    result_list = []

    result_list.append(Premises.objects.order_by('?').first())
    result_list.append(Food.objects.order_by('?').first())
    result_list.append(AgencyDecoration.objects.order_by('?').first())
    result_list.append(Agency.objects.order_by('?').first())

    return(result_list)

