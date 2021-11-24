from .cart import Cart
from django.http import JsonResponse
from django.shortcuts import render
from premises.models import Premises
from animators.models import Agency, Animator
from restaurants.models import Restaurant, Food
from decorations.models import AgencyDecoration, Decoration
from django.shortcuts import get_object_or_404

# Create your views here.
def indexView(request):
    return render(request, 'index.html', {})

def cartView(request):
    return render(request, 'cart.html', {})

def AddCart(request):
    responseData  = {}
    slug = str(request.POST.get('slug', None))
    model_name = str(request.POST.get('model_name', None))
    quantity = request.POST.get('quantity', None)
    product_id = request.POST.get('product_id', None)
    model = globals()[model_name.capitalize()]
    # ------------------------------
    cart = Cart(request)
    product = get_object_or_404(model, id = product_id)
    cart.add(product=product, option=model_name, slug=slug, quantity=quantity)

    return JsonResponse(responseData)

def OutputModalData(request):
     result = ''
     model_name = request.POST.get('model', None)
     slug = request.POST.get('slug', None)
     product_id = request.POST.get('product_id', None)
     model = globals()[model_name.capitalize()]
     product = get_object_or_404(model, id = product_id)
     result = '<div class="modal-add-cart"><div class="close"><i class="fas fa-times"></i></div><div class="main-part"><div class="main-block"><div class="title"><h2>' + product.title + '</h2>'
     if model_name == 'animator':
        result += '<span>' + str(product.duration) +'ч</span>'
     elif model_name == 'food':
        result += '<span>' + str(product.duration) + 'г</span>'
     result += '</div><div class="description"><ul>' + product.description + '</ul></div><div class="characteristics-block"><div class="characteristics"><p>' + product.structure + '</p></div><div class="feature"><i class="fas fa-shopping-cart"></i><p>' +  product.delivery + '</p></div></div></div><div class="img-container"><img src="' + product.image.url + '" alt="Image"></div></div><textarea name="order_comment" id="order_comment">Ваши пожелания и комментарии к заказу</textarea><div class="buttons-block"><button class="add_cart" data-product="' + str(product.id) + '" data-slug="' + slug + '" data-model="' + model_name + '" data-quantity="1" data-price="' + str(product.price) + '">Добавить в корзину <span>' + str(product.price) + '</span></button><button class="minus">-</button><button class="counter" disabled>1</button><button class="plus">+</button></div></div>'
     responseData  = {
        'result': result,
     }
     return JsonResponse(responseData)


def checkPurchasesViewedItem(request, name, id):
    for item in request.session['viewed_products']:
        if item["title"] == name and item["id"] == id:
            return False

    return True

# Processing sessions for output purchases viewed
def addPurchasesViewed(request, product, model):
    if not request.session.get('viewed_products'):
        request.session['viewed_products'] = list()
    else:
        request.session['viewed_products'] = list(request.session['viewed_products'])

    item_exist = checkPurchasesViewedItem(request, product.title, product.id)
    add_product = {
        'title': product.title,
        'id': product.id,
        'mini_desc': product.mini_desc,
        'link': '/product/' + model + '/' + product.slug,
        'image': product.image.url,
        }

    if item_exist and len(request.session['viewed_products']) < 10:
        request.session['viewed_products'].append(add_product)
        request.session.modified = True
    elif item_exist and len(request.session['viewed_products']) >= 10:
       del request.session['viewed_products'][0]
       request.session['viewed_products'].append(add_product)
       request.session.modified = True

    return  request.session['viewed_products']


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