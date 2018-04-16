#! ../../virtenv/bin/python3
import sys
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
import os

User = get_user_model()
i = 0
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'members.txt')
file = open(file_path,'r')
for line in file:
    uname, fname, lname, eMail, pword = line.split(",")
    try:
        user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=eMail, password=pword)
        user.save()
        i+=1
        print('Created user:' +uname)
    except: #catch all and print
        e = sys.exc_info()[0]
        print(e)
print('Inserted '+ str(i) +'  users successfully into the DB')
file.close()
