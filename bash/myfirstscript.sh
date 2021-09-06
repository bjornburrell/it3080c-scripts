#!/bin/bash

# this is a script that outputs IP address and hostnam
greeting='This is a script, HELLO'
echo $greeting, thanks for joining us!
echo '$greeting, thanks for joining us. You owe me $20'
echo "$greeting, thanks for joining us!"
echo "$greeting, you owe me $20"

echo Machine Type: $MACHTYPE
echo Hostname : $HOSTNAME
echo Working Dir : $PWD
echo Session Length : $SECONDS
echo Home Dir : $HOME


a=$(ip a | grep 'noprefixroute ens192' | awk '{print $2}')
echo MY IP IS $a
