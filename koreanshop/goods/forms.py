from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-input'}) )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = User # прописываем с какой моделью работаем 
        fields = ('username', 'email','password1', 'password2') # прописываем те поля которые мы хотим чтобы отображались 

class EditUserForm(UserChangeForm):
    
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-input'}) )
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-input'}) )
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class':'form-input'}) )
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-input'}))
   

    class Meta:
        model = User # прописываем с какой моделью работаем 
        fields = ('username', 'first_name', 'last_name', 'email', 'password') # прописываем те поля которые мы хотим чтобы отображались 




class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password'}))
    new_password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password'}))

    class Meta:
        model = User # прописываем с какой моделью работаем 
        fields = ('old_password','new_password1', 'new_password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'photo')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
      







    
    
