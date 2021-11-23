from decimal import Decimal
from django.conf import settings
from premises.models import Premises
from animators.models import Agency, Animator
from restaurants.models import Restaurant, Food
from decorations.models import AgencyDecoration, Decoration

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSION_ID)
        if not self.cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = cart
            self.cart['info'] = {'count': 0, 'price': 0, 'sale': 0, 'total_price': 0}
            self.cart['products'] = {}

    def add(self, product, option):
        product_id = str(product.id)
        if product_id not in self.cart['products']:
            self.cart['products'][product_id] = {
                'category': option,
                'title': product.title,
                'price': str(product.price),
                'sale': str(product.sale),
                'link': '/product/' + option + '/' + product.slug,
                'image': product.image.url,
                'quantity': 1,
            }
            self.cart['info']['count'] += 1
            self.prices_calculation(product)
        elif option in self.cart['products'][product_id]['category']:
            self.cart['products'][product_id]['quantity'] += 1
            self.prices_calculation(product)
        else:
            self.cart['products'][product_id] = {
                'category': option,
                'title': product.title,
                'price': str(product.price),
                'sale': str(product.sale),
                'link': '/product/' + option + '/' + product.slug,
                'image': product.image.url,
                'quantity': 1,
            }
            self.cart['info']['count'] += 1
            self.prices_calculation(product)
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def prices_calculation(self, product):
        price = Decimal(self.cart['info']['price'])
        total = Decimal(self.cart['info']['total_price'])
        self.cart['info']['price'] = str(product.price + price)
        if not product.sale:
            self.cart['info']['total_price'] = str(product.price + total)
        else:
            sale = Decimal(self.cart['info']['sale'])
            self.cart['info']['sale'] = str(product.sale + sale)
            self.cart['info']['total_price'] = str(product.sale + total)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True