#! ../../virtenv/bin/python3
import sys, os
from products.models import Purchase_history, Product
from django.contrib.auth.models import User
from datetime import datetime

i = 0
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'purchase_history.txt')
file = open(file_path,'r')
dict = {}
list = User.objects.all()
products_list = Product.objects.all()
prod_dict = {}
for obj in list:
    dict[obj.username] = obj
for prod in products_list:
    prod_dict[prod.name]= prod

for line in file:
    try:
        p_name, p_date, user = line.split(",")
        p_date = datetime.strptime(p_date, '%Y-%m-%d')
        uobj = dict[user.strip('\n')]
        product = prod_dict[p_name]
        ph = Purchase_history(productName=product, date=p_date ,user=uobj)
        ph.save()
        i+=1
        print('Created Purchase_history Product: ' +str(ph.productName) + ' Date: ' + str(ph.date) + ' User: ' + ph.user.username)
    except:
        e = sys.exc_info()
        print(e)
print('Inserted '+ str(i) +'  ph successfully into the DB')
file.close()
