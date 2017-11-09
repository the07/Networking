#! /usr/bin/env python3

import poplib
import getpass

POP3_SERVER = 'pop.googlemail.com'
POP_PORT = 995

def fetch_email(username, password):
    mailbox = poplib.POP3_SSL(POP3_SERVER, POP_PORT)
    mailbox.user(username)
    mailbox.pass_(password)

    num_messages = len(mailbox.list()[1])
    print ('Total emails: {}'.format(num_messages))
    print ('Getting last email: ')
    for msg in mailbox.retr(num_messages)[1]:
        print (msg)
    mailbox.quit()

if __name__ == '__main__':

    username = input('Enter your google ID: ')
    password = getpass.getpass(prompt="Enter your password: ")

    fetch_email(username, password)
