from typing import Any, Dict
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from .utils import *
from .forms import *

menu = [
    {'title': 'KOREAN SHOP', 'url_name' : 'home'},
    {'title': 'Корзина', 'url_name' : 'basket'},
    {'title': 'Избранное', 'url_name' : 'favority'}]



class MainPage(DataMixin, ListView):
    model = Goods
    template_name = 'goods/index.html'
    context_object_name = 'goods'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exctra_con = self.get_user_context(title='Главная страница', cat_selected = 0)
        return dict(list(context.items()) + list(exctra_con.items()))

    def get_queryset(self):
        return Goods.objects.filter(is_published=True)


# параметрт kwargs - все параметры маршрута

class GoodsCategory(DataMixin, ListView):
    model = Goods
    template_name = 'goods/index.html'
    context_object_name = 'goods'

    def get_queryset(self):
        return Goods.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exctra_con = self.get_user_context(title='Категория - ' + str(context['goods'][0].cat),
                                           cat_selected = context['goods'][0].cat_id)

        return dict(list(context.items()) + list(exctra_con.items()))



class GoogPost(DataMixin, DetailView):
    model = Goods
    slug_url_kwarg = 'good_slug' # по умолчанию DetailView обращается к аттрибуту slug, поэтому мы его переопредяляем как нам удобно
    template_name = 'goods/good.html'
    context_object_name = 'goods'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exctra_con = self.get_user_context(title='Категория - ' + str(context['goods']),
                                           cat_selected = context['goods'].cat_id)
     
        return dict(list(context.items()) + list(exctra_con.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'goods/login.html'
    # success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exctra_con = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(exctra_con.items()))
    
    def get_success_url(self): # 
        return reverse_lazy('home')  
    
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'goods/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exctra_con = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(exctra_con.items()))
    
    def form_valid(self, form):
        user = form.save()
        profile = Profile.objects.create(user=user)
        login(self.request, user)
        return redirect('home')
    
class UserEditView(DataMixin, UpdateView):
    form_class = EditUserForm   
    template_name = 'goods/edit.html' 
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exctra_con = self.get_user_context(title='Редактирование User')
        return dict(list(context.items()) + list(exctra_con.items()))


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name='goods/change_password.html'
    success_url = reverse_lazy('home')


class ShowProfilePageView(DataMixin, DetailView):
    model = Profile
    template_name = 'goods/profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exctra_con = self.get_user_context(title='Профиль')
        return dict(list(context.items()) + list(exctra_con.items()))
    
 
class ProfileEditView(DataMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'goods/edit_profile.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exctra_con = self.get_user_context(title='Редактирование Profile')
        return dict(list(context.items()) + list(exctra_con.items()))
    
    # def get_success_url(self): #  сделать редирект на профиль на не на главную страницу
    #     return reverse_lazy('profile:user_id', args=1)
    
    

    
    






    

    
def logout_user(request):
    logout(request)
    return redirect('login')

# def profile(request):
#     return render(request, "goods/profile.html")






    





