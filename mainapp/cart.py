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

    def add(self, product, option=0, slug=0, parent=0, quantity=1):
        product_id = str(product.id)
        str_key = option + product_id
        if str_key not in self.cart['products']:
            self.cart['products'][str_key] = {
                'category': option,
                'product_id': product_id,
                'title': product.title,
                'price': str(product.price),
                'sale': str(product.sale),
                'link': '/product/' + option + '/' + slug,
                'image': product.image.url,
                'quantity': quantity,
            }
            if parent:
               self.cart['products'][str_key]['parent'] = parent

            if option == 'premises':
               self.cart['products'][str_key]['address'] = product.address
            else:
               self.cart['products'][str_key]['address'] = product.delivery

            self.cart['info']['count'] += 1
            self.prices_calculation_plus(product, Decimal(quantity))
        else:
            self.cart['products'][str_key]['quantity'] = str(Decimal(quantity) + Decimal(self.cart['products'][str_key]['quantity']))
            self.prices_calculation_plus(product, Decimal(quantity))
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product, quantity='all'):
        if quantity == 'all':
            self.cart['info']['count'] -= 1
            quantity = self.cart['products'][product]['quantity']
            x = 0
            for key in self.cart['products']:
                if product == key:
                    del self.cart['products'][key]
                    self.save()
                    return
                x += 1
        else:
            self_quantity = self.cart['products'][product]['quantity']
            self.cart['products'][product]['quantity'] = str(Decimal(self_quantity) - Decimal(quantity))
        self.prices_calculation_minus(product, Decimal(quantity))
        self.save()

    def prices_calculation_plus(self, product, quantity):
        price = Decimal(self.cart['info']['price'])
        total = Decimal(self.cart['info']['total_price'])
        self.cart['info']['price'] = str((product.price * quantity) + price)
        if product.sale == 0:
            self.cart['info']['total_price'] = str((product.price * quantity) + total)
        else:
            sale = Decimal(self.cart['info']['sale'])
            self.cart['info']['sale'] = str((product.sale * quantity) + sale)
            self.cart['info']['total_price'] = str((product.sale * quantity) + total)

    def prices_calculation_minus(self, product, quantity):
        price = Decimal(self.cart['info']['price'])
        total = Decimal(self.cart['info']['total_price'])
        product_sale = Decimal(self.cart['products'][product]['sale'])
        product_price = Decimal(self.cart['products'][product]['price'])
        self.cart['info']['price'] = str(price - (product_price * quantity))
        if product_sale == 0:
            self.cart['info']['total_price'] = str(total - (product_price * quantity))
        else:
            sale = Decimal(self.cart['info']['sale'])
            self.cart['info']['sale'] = str(sale - (product_sale * quantity))
            self.cart['info']['total_price'] = str(total - (product_sale * quantity))

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True