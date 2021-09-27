import django

print('hello world')   # Python work
print(django.get_version())   # Django work


'''
python -m pip install Django - install Django
git clone https://github.com/django/django.git - update Django
python -m pip install -e django/ - import Django code
cd ../ - up level in directory
django-admin startproject 'name of project' - create new project
cd 'name of project' - go to 'name of project' directory
python3 manage.py startapp 'name of application' - create new application in django
In main directory of project / settings.py add new application like: 
INSTALLED_APPS = [ 'weather',] - weather new application
clear - clean terminal
python3 manage.py migrate - do migrate
python manage.py createsuperuser - Create Super User with login and password
python manage.py runserver - run server
'''



