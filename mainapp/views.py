import json
from .cart import Cart
from kiddeo.settings import CART_SESSION_ID, STATIC_URL
from django.http import JsonResponse, request
from django.shortcuts import render
from premises.models import Premises
from animators.models import Agency, Animator
from restaurants.models import Restaurant, Food
from blog.models import Blog, Comments
from decorations.models import AgencyDecoration, Decoration
from django.shortcuts import get_object_or_404
from datetime import date

# Create your views here.
def indexView(request):
    return render(request, 'index.html', {})

def ConciergeServiceView(request):
    return render(request, 'concierge_service.html', {})

def AddProductView(request):
    return render(request, 'add_product.html', {})
# Quiz
def quizResultView(request):
    return render(request, 'quiz/result.html', {})

def quizView(request):
    return render(request, 'quiz/quiz.html', {})

def cartView(request):
    cart = Cart(request)
    cart_products = request.session[CART_SESSION_ID]['products'].items()
    cart_info = request.session[CART_SESSION_ID]['info']
    recommendations = productRecommendation()
    listPurchasesViewed = request.session['viewed_products']

    if not listPurchasesViewed:
        listPurchasesViewed = False

    return render(request, 'cart.html',
        {
            'cart_products': cart_products,
            'cart_info': cart_info,
            'recommendations': recommendations,
            'listPurchasesViewed': listPurchasesViewed
        })

def checkoutView(request):
    cart = Cart(request)
    cart_products = request.session[CART_SESSION_ID]['products'].items()
    return render(request, 'checkout.html',
        {
            'cart_products': cart_products
        })

def AddCart(request):
    responseData  = {}
    slug = request.POST.get('slug', None)
    if not slug:
        slug = 0
    parent = request.POST.get('parent', None)
    if not parent:
        parent = 0
    quantity = request.POST.get('quantity', None)
    if not quantity:
        quantity = 1
    model_name = request.POST.get('model_name', None)
    product_id = request.POST.get('product_id', None)
    model = globals()[model_name.capitalize()]
    product = get_object_or_404(model, id = product_id)
    # ------------------------------
    cart = Cart(request)

    cart.add(product=product, option=model_name, parent=parent, slug=slug, quantity=quantity)

    return JsonResponse(responseData)

def DeleteCart(request):
    responseData  = {}
    product = request.POST.get('product', None)
    quantity = request.POST.get('quantity', None)
    if not quantity:
        quantity = 'all'
    # ------------------------------
    cart = Cart(request)

    cart.remove(product=product, quantity=quantity)

    return JsonResponse(responseData)

def OutputModalData(request):
     result = ''
     model_name = request.POST.get('model', None)
     slug = request.POST.get('slug', None)
     parent = request.POST.get('parent', None)
     product_id = request.POST.get('product_id', None)
     model = globals()[model_name.capitalize()]
     product = get_object_or_404(model, id = product_id)
     result = '<div class="modal-add-cart"><div class="close"><i class="fas fa-times"></i></div><div class="main-part"><div class="main-block"><div class="title"><h2>' + product.title + '</h2>'
     if model_name == 'animator':
        result += '<span>' + str(product.duration) +'ч</span>'
     elif model_name == 'food':
        result += '<span>' + str(product.duration) + 'г</span>'
     result += '</div><div class="description"><ul>' + product.description + '</ul></div><div class="characteristics-block"><div class="characteristics"><p>' + product.structure + '</p></div><div class="feature"><i class="fas fa-shopping-cart"></i><p>' +  product.delivery + '</p></div></div></div><div class="img-container" style="background-image: url(' + product.image.url + '); background-size: cover;background-position: center;"></div></div><textarea name="order_comment" id="order_comment">Ваши пожелания и комментарии к заказу</textarea><div class="buttons-block"><button class="add_cart" data-product="' + str(product.id) + '" data-parent="' + parent + '" data-slug="' + slug + '" data-model="' + model_name + '" data-quantity="1" data-price="' + str(product.price) + '">Добавить в корзину <span>' + str(product.sale) + '</span></button><button class="minus">-</button><button class="counter" disabled>1</button><button class="plus">+</button></div></div>'
     responseData  = {
        'result': result,
     }
     if model_name == 'food':
        listPurchasesViewed = addPurchasesViewed(request, product, 'food', slug)
     elif model_name == 'decoration':
        listPurchasesViewed = addPurchasesViewed(request, product, 'decoration', slug)
     else:
        listPurchasesViewed = addPurchasesViewed(request, product, 'animator', slug)
     return JsonResponse(responseData)

# def LoadMoreTabs(request):
#    result = ''
#    model_name = request.POST.get('model', None)
#    offset = request.POST.get('offset', None)
#    parent = request.POST.get('parent', None)
#    product_id = request.POST.get('product', None)
#    model = globals()[model_name.capitalize()]
#    print(parent)
#    audit = model.objects.filter(parent=product_id)[offset:2]

#Purchases
def checkPurchasesViewedItem(request, name, id):
    for item in request.session['viewed_products']:
        if item["title"] == name and item["id"] == id:
            return False

    return True

# Processing sessions for output purchases viewed
def addPurchasesViewed(request, product, model, slug = ''):
    if not request.session.get('viewed_products'):
        request.session['viewed_products'] = list()
    else:
        request.session['viewed_products'] = list(request.session['viewed_products'])

    if model == 'food' or model == 'animator' or model == 'decoration':
        product.slug = slug

    item_exist = checkPurchasesViewedItem(request, product.title, product.id)

    add_product = {
        'title': product.title,
        'id': product.id,
        'mini_desc': product.mini_desc,
        'link': '/product/' + model + '/' + product.slug,
        'image': str(product.image.url),
        }
    if item_exist and len(request.session['viewed_products']) < 10:
        request.session['viewed_products'].append(add_product)
        request.session.modified = True
    elif item_exist and len(request.session['viewed_products']) >= 10:
       del request.session['viewed_products'][0]
       request.session['viewed_products'].append(add_product)
       request.session.modified = True

    return  request.session['viewed_products']

def productRecommendation():

    result_list = []

    result_list.append(Premises.objects.order_by('?').first())
    result_list.append(Food.objects.order_by('?').first())
    result_list.append(Animator.objects.order_by('?').first())
    result_list.append(Decoration.objects.order_by('?').first())
    return(result_list)

#AJAX functions
def SidebarFilters(request):
    result = ''
    offset = request.POST.get('offset', None)
    model_name = request.POST.get('model', None)
    filters = request.POST.get('filters', None)
    order_by = request.POST.get('order_by', None)
    switcher = request.POST.get('switcher', None)
    additional_filters = request.POST.get('additional_filters', None)
    model = globals()[model_name]

    if filters != None:
        filters = json.loads(filters)

    if filters != None and order_by != None:
        if not offset:
            products = model.objects.filter(**filters).order_by(order_by)[:7]
        else:
            products = model.objects.filter(**filters).order_by(order_by)[int(offset):7]
        count = model.objects.filter(**filters).count()
    elif filters != None and order_by == None:
        if not offset:
            products = model.objects.filter(**filters)[:7]
        else:
            products = model.objects.filter(**filters)[int(offset):7]
        count = model.objects.filter(**filters).count()
    elif filters == None and order_by == None:
        if not offset:
            products = model.objects.all()[:7]
        else:
            products = model.objects.all()[int(offset):int(offset) + 7]
        count = model.objects.all().count()
    else:
        if not offset:
            products = model.objects.all().order_by(order_by)[:7]
        else:  
            products = model.objects.all().order_by(order_by)[int(offset):7]
        count = model.objects.all().count()

    #Дополнительный фильтр
    if switcher != None:
        if switcher == 'exclude':
            additional_filters = additional_filters.split('=')
        else:
            additional_filters = additional_filters.split('=')
            times = additional_filters[1].split(' ')
            time_start = times[1]
            time_start = time_start.split(':')
            time_start = int(time_start[0])
            time_end = times[3]
            time_end = time_end.split(':')
            time_end = int(time_end[0])    

    if model_name == 'Premises':
        for product in products:
            if switcher != None:
                #Дополнительный фильтр |
                if switcher == 'exclude':
                    # | Проверка на выходной день
                    day = getattr(product, additional_filters[0])
                    if day != additional_filters[1]:            
                        result += '<div class="premises-card"><div class="wrap-thumbnail"><div class="discount"><h4>Подарок</h4></div>'
                        if not product.video:
                            result += '<img src="' + product.image.url + '" alt="Image">'
                        else:
                            result += '<div class="tap"><i class="fas fa-hand-pointer"></i></div><video controls="false" src="' + product.video.url + '"></video>'
                        result +='</div><div class="premises-card-content"><div class="title-block"><div class="part-one"><h6>x2 бонусы</h6><span><a href="/product/premise/' + product.slug + '" style="width: 100%; height: 100%;">' + product.title + '</a></span><h6>147 оценок 54 отзыва</h6></div><div class="part-two"><i class="far fa-heart"></i></div></div><div class="rating"><h4>4.8</h4><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"></div><div class="parameters"><div class="element"><img src="' + STATIC_URL + 'icons/clock.png' + '"><h4><span>2</span> часа</h4></div><div class="element"><img src="' + STATIC_URL + 'icons/ruble.png' + '">'
                        if product.sale:
                            result += '<h4>от <span>' + str(product.sale) + '</span> за час</h4>'
                        else:
                            result += '<h4>от <span>' + str(product.price) + '</span> за час</h4>'
                        result += '</div><div class="element"><img src="' + STATIC_URL + 'icons/square.png' + '"><h4><span>' + str(product.square) + '</span> кв. м.</h4></div><div class="element"><img src="' + STATIC_URL + 'icons/people.png' + '"></i><h4>' + str(product.count_peoples) + '</h4></div></div><h5>' + product.address + '</h5><div class="map"><iframe src="' + product.map_link + '" frameborder="0"></iframe></div></div></div>'
                    else:
                        count = int(count) - 1
                else:
                    #| Проверка по расписанию
                    day = getattr(product, additional_filters[0])
                    if day != 'Выходной':
                        day_time = day.split(' ')
                        day_time_start = day_time[1].split(':')
                        day_time_start = int(day_time_start[0])
                        day_time_end = day_time[3].split(':')
                        day_time_end = int(day_time_end[0])
                        if time_start >= day_time_start and time_end <= day_time_end:    
                            result += '<div class="premises-card"><div class="wrap-thumbnail"><div class="discount"><h4>Подарок</h4></div>'
                            if not product.video:
                                result += '<img src="' + product.image.url + '" alt="Image">'
                            else:
                                result += '<div class="tap"><i class="fas fa-hand-pointer"></i></div><video controls="false" src="' + product.video.url + '"></video>'
                            result +='</div><div class="premises-card-content"><div class="title-block"><div class="part-one"><h6>x2 бонусы</h6><span><a href="/product/premise/' + product.slug + '" style="width: 100%; height: 100%;">' + product.title + '</a></span><h6>147 оценок 54 отзыва</h6></div><div class="part-two"><i class="far fa-heart"></i></div></div><div class="rating"><h4>4.8</h4><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"></div><div class="parameters"><div class="element"><img src="' + STATIC_URL + 'icons/clock.png' + '"><h4><span>2</span> часа</h4></div><div class="element"><img src="' + STATIC_URL + 'icons/ruble.png' + '">'
                            if product.sale:
                                result += '<h4>от <span>' + str(product.sale) + '</span> за час</h4>'
                            else:
                                result += '<h4>от <span>' + str(product.price) + '</span> за час</h4>'
                            result += '</div><div class="element"><img src="' + STATIC_URL + 'icons/square.png' + '"><h4><span>' + str(product.square) + '</span> кв. м.</h4></div><div class="element"><img src="' + STATIC_URL + 'icons/people.png' + '"></i><h4>' + str(product.count_peoples) + '</h4></div></div><h5>' + product.address + '</h5><div class="map"><iframe src="' + product.map_link + '" frameborder="0"></iframe></div></div></div>'
                        else:
                            count = int(count) - 1         
            else: 
                result += '<div class="premises-card"><div class="wrap-thumbnail"><div class="discount"><h4>Подарок</h4></div>'
                if not product.video:
                    result += '<img src="' + product.image.url + '" alt="Image">'
                else:
                    result += '<div class="tap"><i class="fas fa-hand-pointer"></i></div><video controls="false" src="' + product.video.url + '"></video>'
                result +='</div><div class="premises-card-content"><div class="title-block"><div class="part-one"><h6>x2 бонусы</h6><span><a href="/product/premise/' + product.slug + '" style="width: 100%; height: 100%;">' + product.title + '</a></span><h6>147 оценок 54 отзыва</h6></div><div class="part-two"><i class="far fa-heart"></i></div></div><div class="rating"><h4>4.8</h4><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"></div><div class="parameters"><div class="element"><img src="' + STATIC_URL + 'icons/clock.png' + '"><h4><span>2</span> часа</h4></div><div class="element"><img src="' + STATIC_URL + 'icons/ruble.png' + '">'
                if product.sale:
                    result += '<h4>от <span>' + str(product.sale) + '</span> за час</h4>'
                else:
                    result += '<h4>от <span>' + str(product.price) + '</span> за час</h4>'
                result += '</div><div class="element"><img src="' + STATIC_URL + 'icons/square.png' + '"><h4><span>' + str(product.square) + '</span> кв. м.</h4></div><div class="element"><img src="' + STATIC_URL + 'icons/people.png' + '"></i><h4>' + str(product.count_peoples) + '</h4></div></div><h5>' + product.address + '</h5><div class="map"><iframe src="' + product.map_link + '" frameborder="0"></iframe></div></div></div>'
                                      
    elif model_name == 'Restaurant':
        for product in products:
            product.additional_data = Food.objects.filter(restaurant=product)[:4]
            result += '<div class="foods-card"><div class="title-block"><div class="part-one"><span><a href="/product/food/' + product.slug + '" style="width: 100%; height: 100%;">' + product.title +  '</a></span><div class="discount"><h4>Подарок</h4></div><h4>x2 бонусов</h4></div><div class="part-two"><a href="#">Скачать полное меню</a><i class="far fa-heart"></i></div></div><div class="parameters-panel"><div class="rating"> <h3>4.8</h3><div class="rating-block"><h4>147 оценок 54 отзыва</h4><div class="rating-stars"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"></div></div></div><div class="element"><h4>Мин. стоимость заказа</h4><h3>' + str(product.price) + '₽</h3></div><div class="element"><h4>Принимает заказы</h4><h3>за <span>' + str(product.booking_time) +'</span> ч.</h3></div><div class="element"><h4>Доставка</h4><h3><span>' + str(product.price_departure) + '</span>₽</h3></div><div class="element"><h4>Последний заказ</h4><h3>' + product.last_order + '</h3></div><div class="element"><h4>Обслуживание</h4>'
            if product.service:
                result += '<h3>Включено</h3>'
            else:
                result += '<h3>Не включено</h3>'
            result += '</div></div>'
            if not product.additional_data:
                result += '<div class="empty"><span>Мы скоро откроемся</span></div>'
            result += '<div class="list-images">'
            for food in product.additional_data:
                result += '<div class="slide"><div class="img-wrapper"><img src="' + food.image.url + '" alt="Images"></div><h4>' + food.title + '</h4><div class="price-block">'
                if food.sale:
                    result += '<span class="price">' + str(food.price) + '</span><span class="sale">' + str(food.sale) + '₽</span>'
                else:
                    result += '<span class="price">' + str(food.price) + '</span>'
                result += '</div></div>'
            result += '</div></div>'    
    elif model_name == 'Agency':
         for product in products:
            product.additional_data = Animator.objects.filter(agency=product)[:4]
            result += '<div class="foods-card"><div class="title-block"><div class="part-one"><span><a href="/product/animator/' + product.slug + '" style="width: 100%; height: 100%;">' + product.title + '</a></span><div class="discount"><h4>Подарок</h4></div><h4>x2 бонусов</h4></div><div class="part-two"><a href="#">Скачать полный прайс</a><i class="far fa-heart"></i></div></div><div class="parameters-panel"><div class="rating"><h3>4.8</h3><div class="rating-block"><h4>147 оценок 54 отзыва</h4><div class="rating-stars"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"></div></div></div><div class="element"><h4>Мин. длительность</h4><h3>' + str(product.price) + ' ч.</h3></div><div class="element"><h4>Принимает заказы</h4><h3>за <span>' + str(product.booking_time) + '</span> ч.</h3></div><div class="element"><h4>Последний заказ</h4><h3>' + product.last_order + '</h3></div><div class="element"><h4>Цена за выезд</h4><h3>' +  str(product.price_departure) + '</h3></div></div>'
            if not product.additional_data:
                result += '<div class="empty"><span>Мы скоро откроемся</span></div>'
            result += '<div class="list-images">'
            for animator in product.additional_data:
                result += '<div class="slide"><div class="img-wrapper"><img src="' + animator.image.url + '" alt="Images"></div><h4>' + animator.title + '</h4><div class="price-block">'
                if animator.sale:
                    result += '<span class="price">' + str(animator.price) + '</span><span class="sale">' + str(animator.sale) + '₽</span>'
                else:
                    result += '<span class="price">' + str(animator.price) + '</span>'
                result += '</div></div>'
            result += '</div></div>'
    else:
         for product in products:
            product.additional_data = Decoration.objects.filter(agency=product)[:4]
            result +=  '<div class="foods-card"><div class="title-block"><div class="part-one"><h3><a href="/product/decoration/' + product.slug + '" style="width: 100%; height: 100%;">' + product.title + '</a></h3><div class="discount"><h4>Подарок</h4></div><h4>x2 бонусов</h4></div><div class="part-two"><a href="#">Скачать полный прайс</a><i class="far fa-heart"></i></div></div><div class="parameters-panel"><div class="rating"><h3>4.8</h3><div class="rating-block"><h4>147 оценок 54 отзыва</h4><div class="rating-stars"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"><img src="' + STATIC_URL + 'icons/star_red.png' + '"></div></div></div><div class="element"><h4>Мин. стоимость заказа</h4> <h3>' + str(product.price) + '₽</h3></div><div class="element"><h4>Принимает заказы</h4><h3>за <span>' + str(product.booking_time) + '</span> часа</h3></div><div class="element"><h4>Доставка</h4><h3>от <span>' + str(product.price_delivery) + '</span>₽</h3></div><div class="element"><h4>Последний заказ</h4><h3>' + product.last_order + '</h3></div><div class="element"><h4>Цена за выезд</h4><h3><span>' + str(product.price_departure) + '</span>₽</h3></div></div>'
            if not product.additional_data:
                result += '<div class="empty"><span>Мы скоро откроемся</span></div>'
            result += '<div class="list-images">'
            for decoration in product.additional_data:
                result += '<div class="slide"><div class="img-wrapper"><img src="' + decoration.image.url + '" alt="Images"></div><h4>' + decoration.title + '</h4><div class="price-block">'
                if decoration.sale:
                    result += '<span class="price">' + str(decoration.price) + '</span><span class="sale">' + str(decoration.sale) + '₽</span>'
                else:
                    result += '<span class="price">' + str(decoration.price) + '</span>'
                result += '</div></div></div></div>'

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
        result += '<div class="product"><div class="product-block"><h3>' + product.title + '</h3><div class="product-desc"><div class="desc"><p>' + product.mini_desc + '</p><span>' + str(product.duration)  + 'ч</span></div><div class="price">'
        if product.sale:
            result += '<span class="sale">' + str(product.price) + '₽</span><span>' + str(product.sale) + '₽</span>'
        else:
            result += '<span>' + str(product.price) + '₽</span>'
        result += '</div></div></div><div class="img-container"><img src="' + product.image.url + '" alt="Image"></div></div>'
    responseData  = {
        'products': result,
    }
    return JsonResponse(responseData)

def AddComment(request):
    name = request.POST.get('name', None)
    title = request.POST.get('title', None)
    blog = get_object_or_404(Blog, title = title)
    content = request.POST.get('comment', None)
    date_today = date.today()
    comment = Comments.objects.create(
        status = False,
        title_post = blog,
        name = name,
        content = content,
        date = date_today
    )
    return JsonResponse(responseData)