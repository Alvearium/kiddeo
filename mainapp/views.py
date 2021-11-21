from django.shortcuts import render


# Create your views here.
def indexView(request):
    return render(request, 'index.html', {})

def cartView(request):
    return render(request, 'cart.html', {})

def checkPurchasesViewedItem(request, name, id):
    for item in request.session['viewed_products']:
        if item["title"] == name and item["id"] == id:
            return False
            
    return True

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