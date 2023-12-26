# This manifest configures ssh config file

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => "\tPasswordAuthentication no",
  ensure => present,
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => "\tIdentityFile ~/.ssh/school",
  ensure => present,
}
