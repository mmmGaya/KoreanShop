from django.urls import include, path
from .views import *

urlpatterns = [
    path("favorities/", include([
        path('', list_favorities, name='favority'),
        path('<int:id>/add', add_to_favoroties, name='add'),
        path('<int:id>/remove', remove_to_favorities, name='remove'),


        
    ]))


]