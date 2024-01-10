venv:
	python -m venv "venv"
	source venv/bin/activate
	pip install --upgrade pip
	pip install -r requeriments/base.txt

install:
	pip install --upgrade pip
	pip install -r requeriments/base.txt

migrate:
	python manage.py makemigrations users posts registration
	python manage.py migrate

fixture:
	python manage.py createsuperuser

run:
	python manage.py runserver

all: venv install migrate fixture