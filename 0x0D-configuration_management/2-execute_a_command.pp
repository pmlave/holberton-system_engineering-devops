# This script kills a specific given process
exec { 'killmenow':
command => '/usr/bin/pkill -f killmenow'
}