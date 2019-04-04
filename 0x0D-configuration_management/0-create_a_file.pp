# This puppet code will create a new file in /tmp with specified conditions
file { '/tmp/holberton':
     ensure	=> 'file',
     path	=> "/tmp/holberton",
     mode	=> "0744",
     owner	=> "www-data",
     group	=> "www-data",
     content	=> "I love puppet"
}