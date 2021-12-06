# Project 3 Overview
-This script is used to query a device or device list and glean the current version info.

-This uses netmiko which is useful for a network independent way to automate your network infrastructure 

-In this case we want to monitor our environment and ensure all our network infrastructure is running the same version

-This script will login to the device or devices specified, run the comamand 'show version' and then uses textfsm to parse the output and organize the data into a row column format.


```

$ pip install netmiko

```
