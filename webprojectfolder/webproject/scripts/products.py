#! ../../virtenv/bin/python3
import sys
from django.contrib.auth import authenticate
import os
from products.models import Product

i = 0
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'products.txt')
file = open(file_path,'r')
for line in file:
    p_category, p_name, p_price = line.split(",")
    try:
        product = Product(category=p_category, name=p_name, price=p_price)
        product.save()
        i+=1
        print('Created product:' +p_name)
    except:
        e = sys.exc_info()[0]
        print(e)
print('Inserted '+ str(i) +'  products successfully into the DB')
file.close()
