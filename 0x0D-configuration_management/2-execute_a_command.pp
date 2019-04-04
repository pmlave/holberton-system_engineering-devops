# Execute a command with pkill
exec { 'pkill':
     path	=> '/usr/bin',
     command	=> 'pkill -f killmenow',
}