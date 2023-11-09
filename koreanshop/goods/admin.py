from django.contrib import admin

from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'cost', 'content', 'photo', 'cat', 'is_published')
    prepopulated_fields = {'slug':('name', )}
    list_editable = ('is_published',)
    fields = ('name', 'slug', 'cost', 'content', 'photo', 'cat', 'is_published') # меняет расположение полей 


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name', )}

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'phone']









# Register your models here.
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)



