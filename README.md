# firemap
to connect with MONGODB:
 1.pip install pymongo
 2.pip install djongo
 3.in settings.py:
 DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'leafletdatabase',
    }
}
4.python manage.py makemigrations
5.python manage.py migrate
