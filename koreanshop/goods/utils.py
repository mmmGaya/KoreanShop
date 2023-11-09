
from django.shortcuts import get_object_or_404
from .models import *
from django.db.models import Count
from basket.forms import *


menu = [ {'title': 'Избранное', 'url_name' : 'favority'},
    {'title': 'Корзина', 'url_name' : 'basket_list'},]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        basket = AddToBasketForm() # вопросики к этому всему 
        cats = Category.objects.annotate(total = Count('goods')).filter(total__gt=0)
        context['cats'] = cats
        context['menu'] = menu
        context['basket'] = basket
        # if 'cat_selected' not in context:
        #     context['cat_selected'] = 0
        return context