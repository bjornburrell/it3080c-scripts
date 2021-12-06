#this script uses Netmiko to query a network device.. in this case a cisco device running IOS in order to query the device information and store it in a csv
#the script takes a device list and your password and then logs into each switch, runs the command 'show version' to get the device information
#netmiko is a platform agnotsic tool that allows you to programatically interact with networking devices

import threading
import sys
import datetime
import os
import csv

from netmiko import Netmiko
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException

#here we ensure the amount of arguments provided match the amount we require, if they dont we quit the program
if len(sys.argv) != 2:
   print("\nNO ARGUMENT PROVIDED FOR <DEVICE>")
   print("\nPlease provide the following arguments:\n")
   print("\tNetmikoVersionChecker.py <DEVICE/DEVICELIST.txt>\n\n")
   print("\tSample usage: python tNetmikoVersionChecker.py CIN-NET-SW-09S1\n                      python tNetmikoVersionChecker.py CINCINNATI_SWITCHES.txt ")
   print("\n .... Exiting ....\n")
   sys.exit(0)

#get the password and current date time and define the command we are running as well as the filepath and file name 
Password = input("whats your password")
startTime = datetime.datetime.now()
textfsmCommands = ["show version"]
filePath = '/'
fileName = input('Enter a filename for the version report: ')

#netmiko needs this to connect to a device
def DeviceConnect(hostName):
   deviceInfo = { 'ip': hostName,
       	   'username': "bjorn",             
      	   'password': Password + OTP,       
      	   'device_type': "cisco_ios", }  
#print status
   print ('\n .... Connecting to the device ' + hostName + ' .... \n')
#try to connect and if we do run  BackupTextfsmCommands  
   try: 
      net_connect = Netmiko(**deviceInfo)
      BackupTextfsmCommands(net_connect,fileName,filePath)
      net_connect.disconnect()      
   except (NetMikoTimeoutException):                     
      print ('\n .... %s not reachable .... \n' %hostName)
   except (NetMikoAuthenticationException):
      print ('\n .... Authentication Failure on %s .... \n' %hostName)
      
def CSVBackup(fileName,filePath,command,output):
   commandOutput = output[command]
   keysOfOutput = commandOutput[0]
   columns = keysOfOutput.keys()
   csv_file = (filePath + fileName + ".csv")
   if os.path.isfile(csv_file) == True:
      try:
         with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            for data in output[command]:
               writer.writerow(data)
      except IOError:
         print('ERROR: IO ERROR')
   else:
       try:
         with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            for data in output[command]:
               writer.writerow(data)
       except IOError:
            print('ERROR: IO ERROR')

#This runs the command and puts the output into a row column format
def BackupTextfsmCommands(net_connect,fileName,filePath):
   output = {}   
   for x in textfsmCommands:
      commandOutput = (net_connect.send_command(x, use_textfsm = True)) 
      output[x] = {}
      output[x] = commandOutput
   outputKeys = output.keys()

   for command in outputKeys:
      commandOutput = output[command]
      if commandOutput[0] != "":
         CSVBackup(fileName,filePath,command,output)
      else:
         continue

#start the program and see if it should thread or run a single instance depending on if there is a text file or not   
def main():

   if sys.argv[1].find('txt') >= 0:
      with open(sys.argv[1]) as deviceList:
         fileOpened = deviceList.read().split()
      for eachArg in fileOpened:
         my_thread = threading.Thread(target = DeviceConnect, args = (eachArg,))
         my_thread.start()

      main_thread = threading.currentThread()
      for some_thread in threading.enumerate():
         if some_thread != main_thread:
            some_thread.join()

   else:
      for eachArg in range(1,len(sys.argv)):
         DeviceConnect(sys.argv[eachArg])


if __name__ == '__main__':
   main()
   print('File(s) output @ /%s' %fileName)


