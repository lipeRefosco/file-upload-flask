#!/bin/bash

echo "Installing apache2"
apt install apache2
apt install libapache2-mod-wsgi-py3
apt install -y apparmor apturl 
echo ""
echo ""
echo "Installing python3 python3-pip"
apt install python3 python3-pip

echo ""
echo ""
echo "Intalling Flask with pip"
pip install Flask

echo ""
echo ""
echo "Coping 'server' folder into /var/www/html"
rm -r /var/www/html/server/
cp -rfv ./server /var/www/html
mkdir /var/www/html/server/uploads /var/www/html/server/database

echo ""
echo ""
echo "Coping file '000-default.config' into /etc/apache2/sites-available/" 
rm /etc/apache2/sites-available/000-default.config
cp ./infra/000-default.conf /etc/apache2/sites-available/

echo ""
echo ""
echo "Reloading apache2"
service apache2 stop
service apache2 start

echo ""
echo ""
echo "Removing applications files" 
cd ../
rm -r exame_-_admissional_-_raioss.com/
