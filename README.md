##Required
* ####python  
测试有没有python环境：  
Open a command prompt window and type in `python` and press return. If you find yourself in a python shell then you're lucky. If you don't then you'll either need to [install python](http://docs.python.org/2/using/windows.html) and/or configure your path.
* ####django  
测试有没有django环境：   
Type `python -c 'import django'`in the shell prompt. Make sure you can run this Or you'll need to install [django](https://docs.djangoproject.com/en/dev/topics/install/)
  
  
##Main steps of django development
* ####Start the project  
After installed python and django, you can use django-admin to start your django project with below code:  
`django-admin.py startproject yourprojectname`  
you can use `django-admin.py -h` for more help.  
Then, you can type `cd yourprojectname` and `python manage.py runserver` in the shell. Open the chrome and type the `localhost:8000` in the address blank to test.
* ####Start the app
In your project directory, type in `django-admin.py startapp yourappname` to start a app. This will make a directary, in that directory you will find 4 files. And you need to register you app in your project through add you appname to the INSTALLED_APPS in yourprojectname/yourprojectname/setting.py file.
* ####Write the app models
In my opinion, the models designing is the most important in web app development project. You can write your designed models in yourappdirectory/models.py file.
* ####Create your database
The models you wrote in the last part most concern the database.Firstly, you need configure you database setting in the yourprojectname/youtprojectname/setting.py file. In details, you need to configure database of Mysql/Sqlite/Postgresql. Finally you need type `python manage.py syncdb` in shell to create database.
* ####Connecting the django admin to the app  
First, you need to configure the INSTALLED_APP to enable the admin function, it's simple, just uncomment a line. Then you need uncomment 2 lines like `from django.contrib import admin` and `admin.autodiscover()` and in patterns add a line ` url(r'^admin/', include(admin.site.urls)),` in urls.py in the same directory with setting. Finally you need create a file in the app directory named admin.py and let it like this [file](https://github.com/tuesda/django-first/blob/master/blog/admin.py).
* ####Write the URLS VIEWS and templates  
Write urls in projectdirectory and write views in appdirectory and make a template directory in appdirectory and in that directory make a directory named as appdirectoryname, put the template files in that.
* ####Add some style  
Make a directory in appdirectory named static and put style files in that. When you want use style files in some template files, these are you need to-do:  
>At the first line in template file, write this `{% load staticfiles %}`
>You can use static files through link like `{% static 'the path in static directory' %}`  


#####reference:<http://www.netmagazine.com/tutorials/get-started-django>

