# LAB 8 Overview
This is a bash script that I created that checks for a new file within a directory and when there is a new file generated.. it will email that file.

This is a POC as I am trying to wrangle my head around this lovely scanner at work that I am trying to get working. I love printers!

 
Due to TLS 1.2 not being supported on this scanner I manage - Scan to Email is out of the picture. Scan to file server is the only other option. But it would be nice for the users to not have to login to a fileserver when they need to access their scans. So I thought I would setup a python script to automatically upload to sharepoint when a new file is generated. Well, I have MFA enabled within the environment so this is not an option either. I am left with a third option which is to send the scan to a shared folder and put some automation in place there (a raspberry pi) to email the file to a distribution list.

So the workflow will go like this - scanner sends file to SMB share on RaspiPi. Bash script running to detect new files kicks off a command to send the most recent file from a directory 

First.. lets setup out linux machine to be able to email... we will follow this documentation:https://www.howtoforge.com/tutorial/configure-postfix-to-use-gmail-as-a-mail-relay/

I will distill the important commands below...


```

dnf update && dnf install postfix mailx

```


```

nano /etc/postfix/sasl_passwd

```
Add these values and replace the username and pass with your gmail (make sure you enable less secure apps
)
```

[smtp.gmail.com]:587    username@gmail.com:password


```
nano /etc/postfix/main.cf

```
Add these values

```

relayhost = [smtp.gmail.com]:587
smtp_use_tls = yes
smtp_sasl_auth_enable = yes
smtp_sasl_security_options =
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt

```
turn your passwd file into a .db file

```

postmap /etc/postfix/sasl_passwd

```
restart postfix

```

systemctl restart postfix.service

```

send test email

```

mail -s "Test subject" recipient@domain.com

```
Troubleshoot by checking logs


```

less /var/log/mail.log

```

Next we have to setup our bash script

we will create email-alert.sh in /usr/local/bin

```

cd /usr/local/bin

nano email-alert.sh

```

add the following content

```
#!/bin/bash
cd /usr/local/bin/testdir
mostrecentfile=$(ls -t /usr/local/bin/testdir | head -1)
echo "here is the most recent file [${mostrecentfile}]" | mailx -s "New file detected" -a "$mostrecentfile" youremail@gmail.com

```

This script pulls the most recent file from the specified directory and emails it...

We will now use systemmd Path Units to monitor directories (or files, but in this case we are looking to monitor a directory)


Create a file called directory-mon.service in the /etc/systemd/system/ directory with the following contents:


```
[Unit] 
Description="Run script to send email alert"

[Service]
ExecStart=/usr/local/bin/email-alert.sh
```

Create a file called directory-mon.path in the /etc/systemd/system/ directory with the following contents.


```

[Unit]
Description="Monitor a directory file for changes"

[Path]
PathModified=/directory/you/want/to/monitor
Unit=passwd-mon.service

[Install]
WantedBy=multi-user.target


```


You can use the systemd-analyze command with the verify option to check the correctness of your unit files. It will help point out any syntax errors


```

$ sudo systemd-analyze verify /etc/systemd/system/passwd-mon.*
```

Start Your systemd Path Unit and enable at boot

```

$ sudo systemctl start passwd-mon.path

$sudo systemctl enable passwd-mon.path

```


to check logs if our service is working 

```

sudo journalctl -u passwd-mon.path
```





I used the following resources to assist with my development: 
https://www.putorius.net/systemd-path-units.html
https://www.howtoforge.com/tutorial/configure-postfix-to-use-gmail-as-a-mail-relay/
