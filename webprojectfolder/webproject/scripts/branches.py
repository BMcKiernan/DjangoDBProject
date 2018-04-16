#! ../../virtenv/bin/python3

import sys, os
from django.contrib.auth import authenticate
from store.models import Branch, Store
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")


objects = {}
store = Store.objects.first()
i = 0
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'branches.txt')
file = open(file_path,'r')
for line in file:
    name, address, phone = line.split(",")
    try:
        branch = Branch(name=store, branch_address=address, phone_number=phone)
        branch.save()
        i+=1
        print('Created branches:' +str(Branch.branch_address))
    except:
        e = sys.exc_info()
        print(e)
print('Inserted '+ str(i) +' branches successfully into the DB')
file.close()
