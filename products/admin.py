from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductSite(admin.ModelAdmin):
    model = Product
    list_display = ['id','price','discount','current_price']