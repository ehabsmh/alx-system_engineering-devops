# Install Nginx web server (w/ Puppet)

package {'nginx':
	ensure => installed,
	name   => 'nginx',
}

file {'index.nginx-debian.html':
	path    => '/var/www/html/index.nginx-debian.html',
	content => 'Hello World!',
	ensure  => 'present',
}

file_line {'redirect':
	path     => '/etc/nginx/sites-available/default',
	line     => "\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}",
	ensure   => 'present',
	multiple => true,
	after    => 'error_page 404 /custom_404.html;',
}

service {'nginx':
	ensure  => running,
	require => Package['nginx'],
}
