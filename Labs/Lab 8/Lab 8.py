# I used the following sources:
# https://realpython.com/python-send-email/#sending-fancy-emails
# https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/

#import everthing neccesary to scrape the wiki page, we are using BeatifulSoup for easy web scrapping

import requests
from bs4 import BeautifulSoup
#import all we need to email, here we setup a dummy gmail with LESS SECURE APPS = ON

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "wikipediafactsforyou@gmail.com"
receiver_email = input("Type your email and press enter:")
password = "WikiFacts!"


message = MIMEMultipart("alternative")
message["Subject"] = "Did you know?"
message["From"] = sender_email
message["To"] = receiver_email

#send a request to wiki to get latest webpage
response = requests.get(
	url="https://en.wikipedia.org/wiki/Main_Page",
)
soup = BeautifulSoup(response.content, 'html.parser')
#find elements in the response that we are interested in...
#to do so I used the inspect element function of Chrome and scrapped the Did you know... section)

title = soup.find(id="Did_you_know_...")
parent = soup.find(id="mp-dyk").find("ul")
html = parent
email = MIMEText(html, "html")

# Add HTML to MIMEMultipart message
message.attach(email)

# Create connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
 
print("""Please check your junk mail! Your email with today's "Did you know" was sent to: """ + receiver_email)

