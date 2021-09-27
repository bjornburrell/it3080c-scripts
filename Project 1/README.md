#This script is used to remove and install 2 local printers for a non-profit
##the script first deletes the existing printers
###then it checks for the drivers and installs them if they are not present
###then it checks for the port assocciated with the printer and creates it if it's not present
###then it adds the printer
###then it repeats the proccess for printer #2 but uses the generic Windows driver, so no drivers are installed in the second part of the script

###OUTPUTS - list of installed printers
