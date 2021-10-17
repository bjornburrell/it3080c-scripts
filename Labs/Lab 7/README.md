# LAB 7 EXAMPLE
Here is how you can run a Python script that I created, which uses pyftpdlib. 

First, let's install pillow

```bash
$ pip install pyftpdlib
```
We are going to use this ftp library to upload, download, and access files from a server a FTP server spun up using our script!

You can pull down the script from here to try it out on your machine!
```$ git clone git@https://github.com/bjornburrell/it3080c-scripts/tree/main/Labs/Lab 7/
```

Now, change the directory to Lab 7 that we just pulled:

```python3 Lab7.py
```

The syntax above will spin up an FTP server at 0.0.0.0:2121 and we can connect with the user: Bjorn & password: Pa$$W0rd

Now we can download, upload, or access the files to our FTP server for our liking