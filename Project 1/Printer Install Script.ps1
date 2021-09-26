#BJORN BURRELL POWERSHELL PROJECT

#I am the sole IT guy at The Literacy Network of Greater Cincinnati and The Queen City Book Bank with ~20 users...
#They recently moved buildings... and got new printers with the move.
#We do not have AD, so managing via GPO is not an option. We also do not have a print server - though a Raspi running CUPS might be a future project.
#This script will remove the existing printers, then check for HP PCL 6 print drivers.. if they aren't installed it downloads and installs it
#Once the drivers are installed we check for the port, if it doesn't exist we create it.
#Once the port and drivers are configured.. then we add the printer!
#Finally we print the list of printers installed to confirm the installation was succesful
#This really highlights the need for AD



# SOURCES:
#https://docs.microsoft.com/en-us/powershell/module/printmanagement/?view=windowsserver2019-ps
#https://www.action1.com/how-to-install-and-remove-printer-with-powershell-on-windows/
#https://lazyadmin.nl/powershell/install-a-printerport-and-printer-with-powershell/
#https://community.spiceworks.com/topic/2076944-use-powershell-to-install-local-ip-printers
#https://davejlong.com/installing-printers-with-powershell/




#Get printer objects, DELETE each object
Get-WmiObject Win32_Printer | foreach{$_.delete()}

#######################################
# Function to download HP PCL Drivers # 
#######################################



function Install-HPDriver($DriverName) {
  if(Get-PrinterDriver | Where-Object Name -eq $DriverName) { return $true }
  $DriverUri = "https://www.dropbox.com/s/40jdl2ogkogdn9c/win10-x64-hp-universal-pcl6.zip?dl=1"
  $DownloadFile = Join-Path -Path $env:TEMP -ChildPath win10-x64-hp-universal-pcl6.zip
  $DriverTempPath = Join-Path -Path $env:TEMP -ChildPath hp-universal-pcl6

  if ($(Test-Path $DriverTempPath) -eq $false) {
      Invoke-WebRequest -Uri $DriverUri -OutFile $DownloadFile
      Expand-Archive -Path $DownloadFile -DestinationPath $DriverTempPath
  }

  $DriverPath = Join-Path -Path $DriverTempPath -ChildPath hpcu220u.inf
  $PnpUtil = Join-Path -Path $env:windir -ChildPath "System32\pnputil.exe"
  & "$PnpUtil" /add-driver $DriverPath
  Add-PrinterDriver -Name $DriverName
}

########################################
# Set veriables for HP Printer install #
########################################

$HPportName = "TCPPort:192.168.1.101"
$HPprintDriverName = "HP Universal Printing PCL 6"
$HPportExists = Get-Printerport -Name $HPportname -ErrorAction SilentlyContinue
$HPipadd = "192.168.1.101"

#check if port exists, if not then add it
if (-not $HPportExists) {
  Add-PrinterPort -name $HPportName -PrinterHostAddress $HPipadd
}
#Check to see if printer driver exists, if it does then add the printer... if not install it using the function above. Finally add the printer.
$HPprintDriverExists = Get-PrinterDriver -name $HPprintDriverName -ErrorAction SilentlyContinue
if ($HPprintDriverExists) {
    Add-Printer -Name "HP Printer" -PortName $HPportName -DriverName $HPprintDriverName
}else
{
Install-HPDriver -DriverName "HP Universal Printing PCL 6"
Add-Printer -Name "HP Printer" -PortName $HPportName -DriverName $HPprintDriverName
}


#############################################
# Set veriables for Lanier Printer install  #
#############################################

$portName = "TCPPort:192.168.1.102"
$printDriverName = "Generic / Text Only"
$portExists = Get-Printerport -Name $portname -ErrorAction SilentlyContinue
$ipadd = "192.168.1.102"

if (-not $portExists) {
  Add-PrinterPort -name $portName -PrinterHostAddress $ipadd
}
$printDriverExists = Get-PrinterDriver -name $printDriverName -ErrorAction SilentlyContinue
if ($printDriverExists) {
    Add-Printer -Name "Lanier Printer" -PortName $portName -DriverName $printDriverName
}else
{
Write-Host "Error Lanier was not added"}

Get-Printer
