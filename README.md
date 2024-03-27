[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/mxgxu2b2)

Configuration for collaborative work:

1) Have postgresql installed in version 16.2 (password "admin")

2) Have postgresql in environment variables

3) Create the hiring_module database for local use

> psql -U postgres

> CREATE DATABASE hiring_module;

4) Have python installed since version 3.12.1

5) Create a virtual python environment (in a location other than the repository or project directory)

>python -m venv hiring_venv

**From here the steps will be necessary every time you work on the project**

6) Activate the virtual environment

> ./hiring_venv/Scripts/activate

When you are in the virtual environment you can work on the project

7) Make the necessary installations of dependencies

> pip install -r requirements.txt

> cd hiring_module

8) Make database migrations

Being in the project directory...

> python manage.py makemigrations

> python manage.py migrate

9) Run server
Being in the project director...

> python manage.py runserver