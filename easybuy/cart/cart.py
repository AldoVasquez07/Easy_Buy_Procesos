from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()


    def get_total_price(self):
        total = Decimal('0.00')
        for item in self.cart.values():
            price = Decimal(item['price'])
            quantity = item['quantity']
            
            # Comprobar si el producto tiene una oferta asociada
            if item.get('oferta'):  # Si la oferta está presente
                oferta = item['oferta']
                descuento = oferta.descuento  # El descuento es un valor porcentual
                if descuento:
                    # Aplicar el descuento: (precio * (1 - descuento / 100))
                    price = price * (1 - Decimal(descuento) / 100)
            
            # Sumar al total el precio por la cantidad de productos
            total += price * quantity
        
        return total