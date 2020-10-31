#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'example@gmail.com'
receiversEmail = ['example@gmail.com']
receiversPhone = ['example@vtext.com']

def sendEmail(message, simpleMessage):
    # ", ".join(receivers)


    introMessage = """\
    <h2>Hello,</h2>
    <h3>Crypto watcher bot reporting daily currency updates:</h3>
    <h1>Crypto Currency Report:</h1>"""


    try:

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiversEmail[0]
        msg['Subject'] = 'Crypto-Currency Daily Report'
        part1 = MIMEText(introMessage, 'html')
        part2 = MIMEText(message, 'html')
        msg.attach(part1)
        msg.attach(part2)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login("", "")
        server.sendmail(sender, receiversEmail, msg.as_string())
        msgPhone = MIMEMultipart()
        part3 = MIMEText(simpleMessage, 'html')
        msgPhone.attach(part3)
        server.sendmail(sender, receiversPhone, msgPhone.as_string())
        print "Emails Sent Successfully"
        server.close()
    except:
       print "Error: Unable to send email to target recipient"