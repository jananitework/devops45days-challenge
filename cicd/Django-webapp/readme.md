# Django Webapp

### 1.1. Install python, pip 

- By default azure Ubuntu vms comes with python3 preinstalled.
```
azureuser@vm1-django-code:~$ python3 -V
Python 3.10.6
```

- Install pip using apt

```
azureuser@vm1-django-code:~$ pip -V
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```

### 1.2. Install django

Command : ``` sudo apt install python3-django ```
```
azureuser@vm1-django-code:~$ django-admin --version
4.2.3
```

### 1.3. Developing a basic django app

#### Step1 :  Create a django project

- Clone the git repo and go to the path "devops45days-challenge/cicd/Django-webapp/"
- Command : ``` django-admin startproject projectcicd ```
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/7c58bab5-5082-42c2-bb8b-50ade52565c3)

- Let’s verify if Django project works. Go to the path /devops45days-challenge/cicd/Django-webapp/projectcicd/ and run ``` python3 manage.py runserver 0.0.0.0:8000``` 
- Allow inbound traffic for port 8080 in azure portal.
- Get the public ip of the Azure vm and check the browser for http://pubilc-ip:8080
- If you see the following error **DisallowedHost at /**, add ALLOWED_HOSTS = ['*'] in `**/devops45days-challenge/cicd/Django-webapp/projectcicd/settings.py**
- Rerun the server

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/99882de6-c122-4bbb-a454-201fd9a10cb2)

- Now check the browser
![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/54eb3294-6dbf-4eea-972e-87d74d2c4fa0)

#### Step2 : Create an application in django

- Command ``` python3 manage.py startapp samplewebapp ```
You should see new folder and files for samplewebapp

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/3eba0523-c6a7-4c48-a6f2-f2dda05ae6c2)

 #### Step3 : Push the code till now to the git repo. 


 #### Step4 : Lets create a samplewebapp with a simple html page


1. Code changes in the app folder
- To create a html page , add a new folder template in the newly created app folder and create a new file demo.html
``` devops45days-challenge/cicd/Django-webapp/projectcicd/samplewebapp/templates/demo.html ```
- Create a new file urls.py in the app folder for rendering the html file and also make necessary changes in views.py
``` /devops45days-challenge/cicd/Django-webapp/projectcicd/samplewebapp/urls.py```


2. Code changes in project folder
- Add the path for the newly created template in settings.py
``` 'DIRS': [os.path.join(BASE_DIR, 'samplewebapp/templates')], ```
- Make changes in the urls.py to redirect the request to the app folder urls.py

3. Rerun the server and you should see the newly created html page in browser

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/482bcb36-e977-47bd-8a7b-f35bb5c29ca3)

4. Push the code changes

Refer to : https://github.com/jananitework/devops45days-challenge/commit/4953b453782f75279c20327c3710e655d95f33d0

### 1.4. Create a docker file

