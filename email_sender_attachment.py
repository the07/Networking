#! /usr/bin/env python3

import os
import getpass
import re
import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(sender, recipient):
    """ Send email with attachment. """

    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    subject = input('Enter the subject: ')
    msg['Subject'] = subject
    message = input('Enter your email message, press enter when done.')
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)

    # Attach an image
    filename=input('Enter the filename of a GIF Image: ')
    path = os.path.join(os.getcwd(), filename)
    if os.path.exists(path):
        img = MIMEImage(open(path, 'rb').read(), _subtype="gif")
        img.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(img)

    # create an smptp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()

    # Send email
    password = getpass.getpass(prompt="Enter your password: ")
    session.login(sender, password)

    session.sendmail(sender, recipient, msg.as_string())
    print ("Your mail has been sent to {}".format(recipient))
    session.quit()

if __name__ == '__main__':

    sender = input("Enter your email address: ")
    recipient = input("Enter recipient's email address: ")

    send_email(sender, recipient)
