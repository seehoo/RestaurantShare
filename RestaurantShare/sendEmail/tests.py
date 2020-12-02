from django.test import TestCase

# Create your tests here.
import smtplib

gmail_user = 'seehoo12345@gmail.com'
gmail_password = 'qzepsjefvsgvctcs'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    
except:
    print('Wrong')