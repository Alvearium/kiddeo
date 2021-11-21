from django.http import JsonResponse
from django.shortcuts import render
from premises.models import Premises
from animators.models import Agency, Animator
from restaurants.models import Restaurant, Food
from decorations.models import AgencyDecoration, Decoration

# Create your views here.
def indexView(request):
    return render(request, 'index.html', {})

def cartView(request):
    return render(request, 'cart.html', {})

#AJAX functions
def SplitStringAndFilteringWithoutOrder(string, model):
    if ',' in string:
        array = dict(e.split('=') for e in string.split(','))
        products = model.objects.filter(**array)
        count = model.objects.filter(**array).count()
    else:
        array = string.split('=')
        products = model.objects.filter(array)
        count = model.objects.filter(array).count()
    return [products, count]

def SplitStringAndFilteringWithOrder(string, order_by, model):
    if ',' in string:
        array = dict(e.split('=') for e in string.split(','))
        products = model.objects.filter(**array).order_by(order_by)
        count = model.objects.filter(**array).count()
    else:
        array = string.split('=')
        products = model.objects.filter(array).order_by(order_by)
        count = model.objects.filter(array).count()
    return [products, count]

def SidebarFilters(request):
    result = ''
    model_name = request.POST.get('model', None)
    filters = request.POST.get('filters', None)
    order_by = request.POST.get('order_by', None)
    model = globals()[model_name]
    if filters != None and order_by != None:
       func_data = SplitStringAndFilteringWithOrder(filters, order_by, model)
       products = func_data[0]
       count = func_data[1]
    elif filters != None and order_by == None:
       func_data = SplitStringAndFilteringWithoutOrder(filters, model)
       products = func_data[0]
       count = func_data[1]
    else:
       products = model.objects.all().order_by(order_by)
       count = model.objects.all().count()

    if model == 'Premises':
        for product in products:
            result += product.title + '<div class="premises-card"><div class="wrap-thumbnail"><div class="discount"><h4>Подарок</h4></div><div class="tap"><i class="fas fa-hand-pointer"></i></div><div class="camera"><i class="fas fa-video"></i></div><img src="https://imgholder.ru/1920x1080/8493a8/adb9ca&text=IMAGE+HOLDER&font=kelson" alt="Image"> <div class="blackout"></div></div><div class="premises-card-content"></div></div>'
    else:
        for product in products:
            result += product.title + '<div class="foods-card"><a href="/product/animator/{{agency.slug}}" style="width: 100%; height: 100%;">f</a></div>'

    responseData  = {
        'objects': result,
        'count': count
    }
    return JsonResponse(responseData)

def MiniProductsCategoryFilter(request):
    result = ''
    model_name = request.POST.get('model', None)
    category = request.POST.get('category', None)
    model = globals()[model_name]
    products = model.objects.filter(subcategory=category)
    for product in products:
        result += '<div class="product"><div class="product-block"><h3>' + product.name + '</h3><div class="product-desc"><div class="desc"><p>' + product.mini_description + '</p><span>' + str(product.duration)  + 'ч</span></div><div class="price">'
        if product.sale:
            result += '<span class="sale">' + str(product.sale) + '₽</span><span>' + str(product.price) + '₽</span></div></div></div><div class="img-container"><img src="' + product.image.url + '" alt="Image"></div></div>'
    responseData  = {
        'products': result,
    }
    return JsonResponse(responseData)