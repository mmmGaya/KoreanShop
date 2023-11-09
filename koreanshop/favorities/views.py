from django.shortcuts import redirect, render
from goods.models import *
from basket.forms import AddToBasketForm

menu = [ {'title': 'Избранное', 'url_name' : 'favority'},
    {'title': 'Корзина', 'url_name' : 'basket_list'},]

def list_favorities(request): 
    if  request.session.get('favorities'):
        fav_id = list(request.session['favorities'])
        fav = Goods.objects.filter(id__in = fav_id)
        basket = AddToBasketForm()
    else:    
        fav = 0
        basket = None
    return render(request, 'favorities/favority.html', {'fav': fav, 'basket':basket, 'title':'Избранное', 'menu':menu })


def add_to_favoroties(request, id):
    if request.method == 'POST':
        if not request.session.get('favorities'):
            request.session['favorities'] = list()
        else:
            request.session['favorities'] = list(request.session['favorities'])

        fav_id_list = [ i for i in request.session['favorities']]

        if id not in fav_id_list:
            request.session['favorities'].append(id)
            request.session.modified = True
    
    return redirect('favority')

def remove_to_favorities(request, id):
    for fav_id in request.session['favorities']:
        if fav_id == id:
            request.session['favorities'].remove(fav_id)

    if not request.session['favorities']:
        del request.session['favorities']

    request.session.modified = True
    return redirect('favority')





