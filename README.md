Install requirements
windows: pip install -r requirements.txt
Mac: pip3 install -r requirements.txt

Migrate database
windows: python manage.py migrate
Mac: python3 manage.py migrate

Run code
windows: python manage.py runserver
Mac: python3 manage.py runserver

Update language
django-admin makemessages -l hi
django-admin makemessages -l mr
django-admin makemessages -l ml
django-admin makemessages -l kn

Update translations
django-admin compilemessages