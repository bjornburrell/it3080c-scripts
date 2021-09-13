#Powershell script for Project 3 in IT3038c
#Bjorn Burrell

function getIP 
{

(Get-NetIPAddress).IPv4Address | Select-String "192"

}

function getDate
 
{

(Get-Date)

}

$IP = getIP
$USER = $env:USERNAME
$HOSTNAME = $env:COMPUTERNAME
$PSV = $Host.Version.Major
$DATE = getDate
$BODY = "This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. Powershell version is $PSV. The date is $DATE."

#Write-Host("This machine's IP is $IP")
#Write-Host("Test... $Body")

Send-MailMessage -To "burrelbn@mail.uc.edu" -From "bjorn746@gmail.com" -Subject "IT3038C Project 3" -Body $BODY smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)