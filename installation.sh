#!/bin/bash

echo "Installing apache2"
apt install apache2

echo "Installing python3 python3-pip"
apt install python3 python3-pip

echo "Intalling Flask with pip"
pip install Flask

echo "Coping 'server' folder into /var/www/html"
cp -rfv ./server /var/www/html

echo "Coping file '000-default.config' into /etc/apache2/sites-available/" 
cp ./infra/000-default.conf /etc/apache2/sites-available/

echo "Reloading apache2"
service apache2 reload