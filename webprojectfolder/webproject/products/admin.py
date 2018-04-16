from django.contrib import admin
from .models import Product, Purchase_history
# Register your models here.

from django import template

admin.site.register(Product)
admin.site.register(Purchase_history)

