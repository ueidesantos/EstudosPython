# -*- coding: utf-8 -*-
'''
Author: Ueide Santos
Create date: 02/04/2020
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


gmail_user = 'usjunior@gmail.com'
gmail_pwd = "hjkvizoobppxclel"
TO = gmail_user
SUBJECT = "título teste"
TEXT = "CORPO EMAIL TESTE"


smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_pwd)



x=0
while x<10:
    smtpserver.sendmail(gmail_user, [TO], TEXT + ' ' + str(x) )
    print('email ' + str(x) + ' enviado.')
    x+=1
    