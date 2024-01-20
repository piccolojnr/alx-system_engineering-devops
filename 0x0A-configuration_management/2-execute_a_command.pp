#!/usr/bin/pup
# Install an especific version of flask (2.1.0)

exec { 'kill_process':
  command   => 'pkill -f killmenow',
  path      => ['/usr/bin', '/usr/sbin'],
  returns   => ['0', '1'],
  logoutput => true,
}
