# ssh_config.pp
include stdlib

file_line { 'Turn off password auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    replace =>  true,
}


file_line { 'Declare file':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentfyFile ~./ssh/school',
    replace =>  true,
}
