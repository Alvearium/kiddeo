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

    def add(self, product, option, slug, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart['products']:
            self.cart['products'][product_id] = {
                'category': option,
                'title': product.title,
                'price': str(product.price),
                'sale': str(product.sale),
                'link': '/product/' + option + '/' + slug,
                'image': product.image.url,
                'quantity': quantity,
            }
            self.cart['info']['count'] += 1
            self.prices_calculation_plus(product, Decimal(quantity))
        elif option in self.cart['products'][product_id]['category']:
            self.cart['products'][product_id]['quantity'] += Decimal(quantity)
            self.prices_calculation_plus(product, Decimal(quantity))
        else:
            self.cart['products'][product_id] = {
                'category': option,
                'title': product.title,
                'price': str(product.price),
                'sale': str(product.sale),
                'link': '/product/' + option + '/' + slug,
                'image': product.image.url,
                'quantity': quantity,
            }
            self.cart['info']['count'] += 1
            self.prices_calculation_plus(product, Decimal(quantity))
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product, option):
        product_id = str(product.id)
        self.cart['info']['count'] -= 1
        self.prices_calculation_minus(product)
        x = 0
        for key in self.cart['products']:
            if product_id == key:
                if option in self.cart['products'][key]['category']:
                    del self.cart['products'][key]
                    self.save()
                    return
            x += 1

    def prices_calculation_plus(self, product, quantity):
        price = Decimal(self.cart['info']['price'])
        total = Decimal(self.cart['info']['total_price'])
        self.cart['info']['price'] = str((product.price * quantity) + price)
        if not product.sale:
            self.cart['info']['total_price'] = str((product.price * quantity) + total)
        else:
            sale = Decimal(self.cart['info']['sale'])
            self.cart['info']['sale'] = str((product.sale * quantity) + sale)
            self.cart['info']['total_price'] = str((product.sale * quantity) + total)

    def prices_calculation_minus(self, product, quantity):
        price = Decimal(self.cart['info']['price'])
        total = Decimal(self.cart['info']['total_price'])
        self.cart['info']['price'] = str(price - product.price)
        if not product.sale:
            self.cart['info']['total_price'] = str(total - product.price)
        else:
            sale = Decimal(self.cart['info']['sale'])
            self.cart['info']['sale'] = str(sale - product.sale)
            self.cart['info']['total_price'] = str(total - product.sale)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True