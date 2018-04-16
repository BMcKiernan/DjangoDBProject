import os,sys,random
from django.contrib.auth.models import User
from store.models import Branch, Sale
from products.models import Purchase_history

purchases = Purchase_history.objects.all()
branches = Branch.objects.all()
dict = {}
for Branch in branches:
    dict[Branch] = (0)
i = 0
for p in range(0, len(purchases)):
    b_no = random.randrange(0,len(branches))
    purch = purchases[p]
    branch = branches[b_no]
    try:
        sale = Sale(branch = branch, sales=purch)
        dict[branch] = (dict.get(branch) + 1)
        sale.save()
        i+=1
        print('Successfully added Sale('+str(branch)+','+str(purch)+')') 
    except:
        e = sys.exc_info()
        print(e)
print('Successfully added ' + str(i) + ' sales.')
for key in dict.keys():
    print(str(key) + ' had ' + str(dict[key]) + ' sales.')
