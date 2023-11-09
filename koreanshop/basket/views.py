from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST

from goods.models import Goods
from .basket import Basket
from .forms import *

menu = [ {'title': 'Избранное', 'url_name' : 'favority'},
    {'title': 'Корзина', 'url_name' : 'basket_list'},]


@require_POST
def add_to_basket(request, good_id):
    basket = Basket(request)
    good = get_object_or_404(Goods, id=good_id)
    form = AddToBasketForm(request.POST)
    if form.is_valid():
        bs = form.cleaned_data
        basket.add(good=good, 
                   quantity=bs['quantity'],
                   update_quant=bs['update'])
        
    return redirect('basket_list')
    
    


def remove_to_basket(request, good_id):
    basket = Basket(request)
    good = get_object_or_404(Goods, id=good_id)
    basket.remove(good)
    return redirect('basket_list')

def basket_list(request):
    basket = Basket(request)
    return render(request, 'basket/list_basket.html', {'basket': basket, 'title':'Корзина', 'menu':menu})
    