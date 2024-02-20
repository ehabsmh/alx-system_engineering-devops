# Change the ulimit to 2000
exec { 'Set ulimit to 2000':
    path    => '/bin:/usr/bin',
    command => "sed -i 's/15/2000/' /etc/default/nginx"
}

# Apply nginx changes
exec { 'restart nginx':
    command => '/usr/sbin/service nginx restart'
}
