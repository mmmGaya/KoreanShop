from django.conf import settings
from decimal import Decimal

from goods.models import Goods

class Basket(object):

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.CART_SESSION_ID)
        if not basket:
            basket = self.session[settings.CART_SESSION_ID] = dict()
        self.basket = basket

    def add(self, good, quantity=1, update_quant=False):

        basket_id = str(good.id)
        if basket_id not in self.basket:
            self.basket[basket_id] = {'quantity': 0,
                                      'price': str(good.cost)}
            
        if update_quant:
            self.basket[basket_id]['quantity'] = quantity
        else:
            self.basket[basket_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.basket
        self.session.modified = True

    def remove(self, good):

        basket_id = str(good.id)
        if basket_id in self.basket:
            del self.basket[basket_id]
            self.save()

    # Зачем нужен метод iter и вообще как он работает 

    def __iter__(self):
        goods_ids = self.basket.keys()
        goods = Goods.objects.filter(id__in=goods_ids)
        for g in goods:
            self.basket[str(g.id)]['good'] = g

        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item 

    def __len__(self):
        return sum(good['quantity'] for good in self.basket.values())
    
    def get_total_price(self):
        return sum(Decimal(good['price']) * good['quantity'] for good in self.basket.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


