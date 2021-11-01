# LAB 8 Overview
This Python script that I created that checks for a new file within a directory and when there is a new file generated.. it will email that file.

This is a POC as I am trying to wrangle my head around this lovely scanner at work that I am trying to get working. I love printers!

 
Due to TLS 1.2 not being supported on this scanner I manage - Scan to Email is out of the picture. Scan to file server is the only other option. But it would be nice for the users to not have to login to a fileserver when they need to access their scans. So I thought I would setup a python script to automatically upload to sharepoint when a new file is generated. Well, I have MFA enabled within the environment so this is not an option either. I am left with a third option which is set up some email forwarding within Gmail.. I will enable les ecure apps then automatically forward any email I get to an email within the orgnazition that has a PowerAutomate script setup to auto upload anything from a certain sender to a shared folder.

So the workflow will go like this - scanner sends file to SMB share on RaspiPi. Bash script running to detect new files kicks off a python script that emails the newest file in the SMB share to an email within the org that will upload any email from the RaspiPi to a Sharepoint folder. 

To get this working you have to run 

```
nohup bash /script/directory/newfile.sh </dev/null >/dev/null 2>&1 &
```

I used the following resources to assist with my development: 
https://stackoverflow.com/questions/1015678/get-most-recent-file-in-a-directory-on-linux
https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/
https://imyuvii.com/posts/watch-directory-file-creation-slack/