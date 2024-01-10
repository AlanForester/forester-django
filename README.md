# Forester

**A django web blog [forester.pro](https://forester.pro)**

Requeriments:

- Install python.
- Create virtual environment. ~> python -m venv "namevenv"
- Install pip. ~> python -m pip install --upgrade pip
- Install dependencies. ~> pip install "package" -> Show requeriments/base.txt
- Create database postgres ~> DB and account user admin
- Migrate models to database. ~> python manage.py makemigrations users adnews registration
- Execute migrations ~> python manage.py migrate
- Create account superuser admin. ~> python manage.py createsuperuser
- Run server. ~> python manage.py runserver 
- Server ~> http://127.0.0.1:8000