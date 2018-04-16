from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product, Purchase_history
from store.models import Sale
from django.shortcuts import render, redirect, get_object_or_404
from .filters import ProductFilter

# Create your views here.


def home(request):
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)
    return render(request, 'products.html', {'filter': product_filter})

@login_required
def user_purchase_history(request):
    current_user = request.user
    all_sales = Sale.objects.all()
    all_purchases = Purchase_history.objects.all()
    qs = all_purchases.filter(user__id=current_user.id)
    final_qs = {}
    if qs:
        strings = []
        for idx, i in enumerate(qs):
            s = Sale.objects.get(sales=i.purchase_no)
            p = i
            strings.append("" + str(current_user) + " purchased " + str(p.productName) + " at " + str(s.branch) + " on " + str(p.date) +" .")
        return render(request, 'Userdata.html', {'strings': strings})
    else:
        return None