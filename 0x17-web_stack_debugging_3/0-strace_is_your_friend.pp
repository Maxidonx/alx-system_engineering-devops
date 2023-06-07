# Install Apache package
package { 'apache2':
  ensure => installed,
}

# Modify Apache configuration file
file { '/etc/apache2/apache2.conf':
  ensure  => present,
  content => template('your_module/apache2.conf.erb'),
  notify  => Service['apache2'],
}

# Restart Apache service
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}
