from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("", MainPage.as_view(), name='home'),
    path("category/<slug:cat_slug>", GoodsCategory.as_view(), name='category'),
    path("good/<slug:good_slug>", GoogPost.as_view(), name='good'),
    path("login/", LoginUser.as_view() , name="login"),
    path("register/", RegisterUser.as_view() , name="register"),
    path("edit/", UserEditView.as_view() , name="edit"), # заводские настройки  
    path("logout/", logout_user, name='logout'),
    path("profile/<int:user_id>", ShowProfilePageView.as_view(), name='profile'),
    path("<int:id>/password/", UserPasswordChangeView.as_view()), 
    path("<int:id>/edit_profile/", ProfileEditView.as_view(), name='edit_profile'), # наши собственные

    

]

