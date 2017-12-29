#!/usr/bin/env sh
clear
echo "----------------Make Compilemessages--------------"
python manage.py compilemessages
echo "----------------Make Migrates--------------"
python manage.py makemigrations
echo "----------------Migrate--------------------"
python manage.py migrate
echo "----------------Run Server-----------------"
python manage.py runserver 0.0.0.0:8700
