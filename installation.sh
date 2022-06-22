#!/bin/bash

echo "Installing apache2"
apt install apache2

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
cp -rfv ./server /var/www/html

echo ""
echo ""
echo "Coping file '000-default.config' into /etc/apache2/sites-available/" 
cp ./infra/000-default.conf /etc/apache2/sites-available/

echo ""
echo ""
echo "Reloading apache2"
service apache2 reload

echo ""
echo ""
echo "Removing applications files" 
cd ../
rm -r exame_-_admissional_-_raioss.com/