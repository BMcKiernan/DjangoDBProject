from django.db import models
from django.contrib.auth.models import User
from products.models import Purchase_history
# Create your models here.

class Store(models.Model):
    hq_address = models.CharField(max_length=80)
    store_name = models.CharField(max_length=80, primary_key=True)

    def __str__(self):
        return 'Store: '+self.store_name

class Branch(models.Model):
    name = models.ForeignKey(Store, on_delete=models.CASCADE)
    branch_address = models.CharField(max_length=80, primary_key=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return 'Branch: '+ self.branch_address

class Sale(models.Model):
    sale_no = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sales = models.ForeignKey(Purchase_history, on_delete=models.CASCADE)

    def __str__(self):
         return 'Sale_no: ' +str(self.sale_no)
