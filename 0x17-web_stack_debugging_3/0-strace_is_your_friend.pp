# Fixes incorrect php extension from "phpp" to "php"
exec { 'fix php extension':
  path    => '/bin/:/usr/local/bin/:/usr/bin/',
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}
