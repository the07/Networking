"""
A simple module to ssh to a specific machine and execute ls command.
Before running the program ensure that the ssh server daemon is ruuning using netstat.
 """

#! /usr/bin/env python3

import getpass
import paramiko

HOSTNAME = 'localhost'
PORT = 22

def run_ssh_cmd(username, password, cmd, hostname=HOSTNAME, port=PORT):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()

    ssh_client.connect(hostname, port, username, password)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)

    print (stdout.read())

if __name__ == '__main__':
    username = input('Enter username: ')
    password = getpass.getpass(prompt="Enter the password")
    cmd = 'ls -l'
    run_ssh_cmd(username, password, cmd)
