# var="sudo apt-get update"
# eval $var

var="pip install --user virtualenv"
eval $var

var="python -m venv ."
eval $var

var="conda deactivate"
eval $var

var="source bin/activate"
eval $var

var="pip install django"
eval $var

var="pip install django-db-file-storage"
eval $var

var="cd src/"
eval $var

var="python manage.py makemigrations"
eval $var

var="python manage.py migrate"
eval $var

var="python manage.py runserver"
eval $var
