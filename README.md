# DjangoDBProject


Instructions to Run Project.
_________________________________________________________________________________
This project needs to be run in linux.

To clone the project type

git clone https://github.com/BMcKiernan/reqsaddedwebproj.git



After cloning the repo 
change directory to webprojectfolder within the DjangoDBProject project folder

Type: source venviv/bin/activate
if you see (venviv) sh4-$ ./PWD/
then you can just cd to webproject and type: "python manage.py runserver" and the the website should work
you just have to hit CTRL and click on the link that appears in the terminal.


If source venviv/bin/activate doesn't work or python manage.py runserver doesn't work
Then you have to create the virtualenv yourself on your computer.
Instructions to create virutalenv yourself: 

First remove the exisiting venviv dir with "rm -rf venviv"
To create the virtualenv type "virtualenv venviv -p python3"

To activate the virtualenv type "source venviv/bin/activate"

To add necessary requirments -type "pip3 install -r requirments.txt"

To run the project locally -
FROM PWD as ./webprojectfolder
sh$- cd webproject
sh$- python manage.py runserver

Then hold CTRL and click the link that is generated in the terminal

For after you've seen the project and want to exit the virutalenv -
sh$- deactivate



Features -
1. Products

   The products button will take you to a list of products where you
   can click the filter button and you can filter the products by 
   price and by name.

   
   You can also add a purchase from the admin part of the site but the reason I wanted
   to add a user based purchase feature is because when you create a user 
   account (which will naturally not have admin privleges)
   and login you will be shown a new button which says User Data.
   
2. User Data
  
   If you create and login as a new user you will have no User Data so this will be blank.
   But notice the cool feature where the User Data button shows only when you've been verified 
 

   If you want to create a user and and create the purchase history through the admin part of the site, 
   Go about creating a user through the sign up part of the website.
   Log in to see that it works.

   To create purchase history for the user you need to create a purchase_history with whatever product you want 
   and the user which you created and know the password for.
   After you create a purchase_history you then need to create a sale, click whatever branch you would like 
   and find the purchase_history pk at the bottom of the list of purchase_history pks in sales. Its the sales foreign key.
  
   The purchase button in the Products section of the front of the website was supposed to automatically get the current user
   the current date and the product and branch they "purchased" it from and generate the sales and purchase_history together at once.


   Once you've created some sales and purchase_histories with your user on the top right of the admin page click view site.
  
   You can click User Data and see my information or you can log out of my user account, 
   log into the one you created and see the newly avaible data under the User Data button.


 3. Log-in Features
   There is restrictions on creating passwords so they are secure 
   and passwords are hashed and stored in my RDS so no one ever sees the actual passwords except the user.
   
   There is a forgot password feature (which may be a little hard to see under the log in screen)
   and if you enter your email you will be emailed a link to reset your password. 
   Because I couldn't set everything up on a ec2 server the email will just appear in the terminal where the website is running
   and you can click the link from there with CTRL.
 

   This will redirect you to the reset password screen and you should just exit out of the tab you just left
   and after resetting your password you can log in from the new tab.
  






     Thanks,
     Brian 
