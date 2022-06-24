#!/bin/bash

# SSL Certicate reference 
# https://serverspace.io/support/help/how-to-get-lets-encrypt-ssl-on-ubuntu/

HOST_NAME=louis.raioss.rocks

# Install tools to configure a SSL Certificate on Let's Encrypt
apt install letsencrypt

# Get the "Let's Encrypt" SSL certificate
certbot certonly --standalone --agree-tos --preferred-challenges http -d $HOST_NAME

# Install tool to autoinstall ssl certificate
apt install python3-certbot-apache

# Execute autoinstaller to host name
certbot --apache --agree-tos --preferred-challenges http -d $HOST_NAME