#!/usr/bin/env bash
# Installs, configures, and starts the web server
HOME_PAGE=\
"<!DOCTYPE html>
<html lang='en-US'>
	<head>
		<title>Home - AirBnB Clone</title>
	</head>
	<body>
		<h1>Welcome to AirBnB!</h1>
	<body>
</html>
"

apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /var/www/html /var/www/error
chmod -R 755 /var/www
echo 'Hello World!' > /var/www/html/index.html
echo -e "Ceci n\x27est pas une page" > /var/www/error/404.html

mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "$HOME_PAGE" > /data/web_static/releases/test/index.html
[ -d /data/web_static/current ] && rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
# bash -c "echo -e '$SERVER_CONFIG' > /etc/nginx/sites-available/default"
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
if [ "$(pgrep -c nginx)" -le 0 ]; then
	service nginx start
else
	service nginx restart
fi
