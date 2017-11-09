#! /usr/bin/env python3
# Listing 1 - First email client
import getpass
import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(sender, recipient):
    """ Send email """

    # Prepare the message
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    subject = input('Enter your email subject: ')
    msg['Subject'] = subject
    message = input('Enter your message, press enter when finished.')
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)

    # Create the smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.set_debuglevel(1)
    session.ehlo()
    session.starttls()
    session.ehlo()
    password = getpass.getpass(prompt="Enter your email password: ")

    # Login to server
    session.login(sender, password)

    # Send the mail
    session.sendmail(sender, recipient, msg.as_string())
    print ('Your mail has been sent to {}'.format(recipient))
    session.quit()

if __name__ == '__main__':
    sender = input("Enter sender email address: ")
    recipient = input("Enter recipient email address: ")
    send_email(sender, recipient)
