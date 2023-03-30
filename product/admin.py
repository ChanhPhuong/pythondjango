
from django.contrib import admin

from product.models import Product
from django.utils.html import format_html

from category.models import Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['categoryId']
    
    def img_tag(self, obj): 
        return format_html('<img src="{}" style="max-width:80px; max-height:60px"/>'.format(obj.image.url))
    list_display = ['name','price','img_tag','categoryId']
admin.site.register( Product, ProductAdmin)
