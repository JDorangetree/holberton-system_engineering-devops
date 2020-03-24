# Manifest to modify SSH config file
file_line { 'refuse to authenticate using a password':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no'
}
file_line { 'configured to use the private key':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/holberton'
}
