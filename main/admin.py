from django.contrib import admin
from main.models import *
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'cat',)

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class BasketAdmin(admin.TabularInline):
    model = BasketCool
    fields = ['product', 'quantity']
    extra = 0
admin.site.register(Category, CatAdmin)
admin.site.register(BasketCool)
# Register your models here.
