#!/usr/bin/puppet apply
# AirBnB clone web server setup and configuration
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin:/usr/sbin:/bin',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

-> file { '/var/www':
  ensure  => directory,
  mode    => '0755',
  recurse => true,
}

-> file { '/var/www/html/index.html':
  content => 'Hello, World!',
}

-> file { '/var/www/error/404.html':
  content => "Ceci n'est pas une page",
}

-> exec { 'make-static-files-folder':
  command => 'mkdir -p /data/web_static/releases/test /data/web_static/shared',
  path    => '/usr/bin:/usr/sbin:/bin',
}

-> file { '/data/web_static/releases/test/index.html':
  content =>
"<!DOCTYPE html>
<html lang='en-US'>
	<head>
		<title>Home - AirBnB Clone</title>
	</head>
	<body>
		<h1>Welcome to AirBnB!</h1>
	<body>
</html>
",
  replace => true,
}

-> exec { 'remove-current':
  command => 'rm -rf /data/web_static/current',
  path    => '/usr/bin:/usr/sbin:/bin',
}

-> file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test/',
  replace => true,
}

-> exec { 'change-data-owner':
  command => 'chown -hR ubuntu:ubuntu /data',
  path    => '/usr/bin:/usr/sbin:/bin',
}

-> file { '/etc/nginx/sites-available/airbnbclone':
  ensure  => present,
  mode    => '0644',
  content =>
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
	server_name _;
	index index.html index.htm;
	error_page 404 /404.html;
	add_header X-Served-By \$hostname;
	location / {
		root /var/www/html/;
		try_files \$uri \$uri/ =404;
	}
	location /hbnb_static/ {
		alias /data/web_static/current/;
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me){
		rewrite ^ https://sketchfab.com/bluepeno/models permanent;
	}
	location = /404.html {
		root /var/www/error/;
		internal;
	}
}",
}

-> file { '/etc/nginx/sites-enabled/airbnbclone':
  ensure  => link,
  target  => '/etc/nginx/sites-available/airbnbclone',
  replace => true,
}

-> service { 'nginx':
  ensure  => running,
}
