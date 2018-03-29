<h1 align="center">
  <br>
  <img src="https://pbs.twimg.com/profile_images/910158554568515584/Gf6WD-iH_400x400.jpg" alt="Fraunhofer" width="300">
  
  <br>
</h1>
<h2 align="center">
  <br>
   <img src="https://teamvirtue.nl/wp-content/uploads/LINQ_Logo_Black-300x138.png" alt="Fraunhofer" width="200">
   <img src="http://www.sollite.net/images/img/2222222-01.jpg" alt="Fraunhofer" width="200">
   <img src="https://upload.wikimedia.org/wikipedia/commons/d/d3/Eindhoven_University_of_Technology_logo.svg" alt="Fraunhofer" width="200">
   <img src="https://cdn.worldvectorlogo.com/logos/fontys-39.svg" alt="Fraunhofer" width="200">
  <br>
</h2>

# Setup
## Prerequisites for development enviorment
1. Make sure you have installed `python` on your machine. [Download Python](https://www.python.org/downloads/)
2. `pip` package manager is installed. If you have a version of `python 2 >= 2.7.9 or Python 3 >= 3.4` you will probably have ``pip`` installed if not [download `pip`](https://www.python.org/downloads/) and in **Terminal** run ``` python get-pip.py```. If you have problems [pip documentation](https://pip.pypa.io/en/stable/installing/)
3. This step is not mandatory but recommended is to make a *python virtual environment* ```sudo pip install virtualenv```
    * Unix based operating systems  
      * Installation of **virtualenv** ```sudo pip install virtualenv```
      * Create a directory to hold the project ```mkdir ~/projectname```
      * Create a virtual environment inside the project folder ```virtualenv nameofprojectenv```
4. PostgreSQL is the database in use so make sure you have it installed.  
    * Unix based operating systems
       *  updating system variables via **Terminal** command ``sudo apt-get update`` 
       *  Installing **PostgreSQL** via **Terminal** command ``sudo apt-get install libpq-dev postgresql postgresql-contrib`` *updating system variables*
       *  Your operating system will make a default user name called ```postgres```  log in with the command ```sudo su - postgres``` 
       *  Creating a new database ```CREATE DATABASE databasename```
       *  Creating a new user ```CREATE USER username WITH PASSWORD 'secret'```
       *  To test if you have installed it correctly use command ```psql -U username -d databasename```
    * Windows operationg systems
       * coming soon!
## Development environment setup
1. Install all requirments run command in the project directory ```pip install -r requirements.txt```
2. Setting up database, add this code to **setings.py**  
    ```ruby
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "databasename",
            "USER": "username",
            "PASSWORD": "secret",
            "HOST": "localhost",
            "PORT": "",
        }
    }
    ```
3. Check if the ```DEBUG = True``` is set in **settings.py**
4. Make migrations for database ```python manage.py makemigrations``` 
5. Migrate **models.py** to postgres with command ```python manage.py migrate```
6. Run a the test server with command ```python manage.py runserver``` this will run the server on the default *port 8000* if that port is taken you can change the port that the test server runs on with ```python manage.py runserver 0.0.0.0:8090```
## Production environment setup
### Coming soon
## Extending a **models.py** for database 
#### Prerequisites
1. Import **models** from framework ```from django.db import models```
2. Import **settings** from framework ```from django.conf import settings```
3. Import **timestampedmodel** from database models ```from django_extensions.db.models import TimeStampedModel```
#### Overview

  **Example**
      ```ruby
       class Example(models.Model):
       city = models.CharField(max_length=50)
       street = models.CharField(max_length=45)
       postcode = models.CharField(max_length=45)
       country = models.CharField(max_length=45)
       nr_Of_Floors = models.IntegerField()
       building_name = models.CharField(max_length=45)
       gender = models.CharField(max_length=1, choices=ENUMGENDER)
      ```
## Extending serializables
#### Overview
**serializable.py** is resopnsible for serializing the data from the orm to json format.
#### Create a new serializable class
1. Importing serializers
   
   **Example**
     ```ruby
     from rest_framework import serializers
     from .models import ModelClass
     ```
2. Creating a new serializable class to json
  
   **Note: That these classes work with *serializers.HyperlinkedModelSerializer* passed as a parameter**
   * serializing all fields
    
    **Example**
      ```ruby
      class ModelClassSerializer(serializers.HyperlinkedModelSerializer):
          class Meta:
              model = ModelClass
              fields = "__all__"
      ```
   * serializing custom fields
    
    **Example**
      ```ruby
      class ModelClassSerializer(serializers.HyperlinkedModelSerializer):
          class Meta:
              model = ModelClass
              fields = ('modelfield', 'modelfield', 'modelfield', 'modelfield')
      ```
## Extending urls
#### Overview
The REST framework supports automatic **urls routing** this is a quick way yo make ulrs.
#### Prerequisites
1. Import **urls** from framework
   
    **Example**
      ```ruby
      from django.conf.urls import url, include
      from django.urls import path
      ```
2. Import **views** from gatherer directory
   
    **Example**
      ```ruby
      from . import views
      ```
#### Router
1. Create a Router
   * DefaultRouter
     
    **Example**
      ```ruby
      router = routers.DefaultRouter()
      ```
   * SimpleRouter
     
    **Example**
      ```ruby
      router = routers.SimpleRouter()
      ```
 2. Register a Serializer
     
    **Example**
      ```ruby
      router.register('url_name', views.ModelClassViewSet)
      ```
3. Add **router** to application urls
     
    **Example**
      ```ruby
      urlpatterns = [
        path('', include(router.urls))
      ]
      ```
## Extending admin
 1. Customizing a admin model
    * Custom class
      
     **Example**
      ```ruby
      class ModelClassAdmin(admin.ModelAdmin):
      list_display = ('modelfield', 'modelfield')
      model = models.ModelClass
      ```
    * Register a custom class
    
     **Example**
      ```ruby
      admin.site.register(models.ModelClass, ModelClassAdmin)
      ```
    * Register with framework default
    
     **Example**
      ```ruby
      admin.site.register(models.ModelClass)
      ```
## Authors

* **Hristiyan Tarnev** - *Initial work* - [Beasteca](https://github.com/beasteca)
* **Martin Savov** - *Initial work* - [MIT120](https://github.com/MIT120)

See also the list of [contributors](https://github.com/teamvirtue/SmartSystemCore/graphs/contributors) who participated in this project.

## License
Copyright (c) <2018> <Team VIRTUE>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
