from django.urls import include, path
from .views import *

urlpatterns = [
    path("basket/", include([
        path('', basket_list, name='basket_list'),
        path('<int:good_id>/add', add_to_basket, name='add_basket'),
        path('<int:good_id>/remove', remove_to_basket, name='remove_basket'),


        
    ]))


]