from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    category = models.CharField(max_length=40)
    name = models.CharField(max_length=40, primary_key=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_category(self):
        return self.category

    def __str__(self):
        return self.name

class Purchase_history(models.Model):
    purchase_no = models.AutoField(primary_key=True)
    productName = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.purchase_no)
