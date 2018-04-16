import django_filters as df
from .models import Product
from django import forms
from django.contrib.auth import models

class ProductFilter(df.FilterSet):
    #category = df.ModelMultipleChoiceFilter(queryset=Product.objects.all(),widget=forms.CheckboxSelectMultiple)
    name = df.CharFilter(lookup_expr='icontains')
    price = df.NumberFilter(name='price',lookup_expr='lte')

    class Meta:
       model = Product
       fields = ['name', 'price',]



