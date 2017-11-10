#! /usr/bin/env python3
import ftplib

FTP_SERVER_URL = 'ftp.kernel.org'
DOWNLOAD_DIR_PATH = '/pub/software/network/tftp'
DOWNLOAD_FILE_NAME = 'tftp-hpa-0.11.tar.gz'

def ftp_file_download(path, username, email):
    # Open a FTP connection
    ftp_client = ftplib.FTP(path, username, email)

    # List the files in the download directory
    ftp_client.cwd(DOWNLOAD_DIR_PATH)
    print ("File list at {}".format(path))
    files = ftp_client.dir()
    print (files)

    # Download a file
    file_handler = open(DOWNLOAD_FILE_NAME, 'wb')
    ftp_client.retrbinary('RETR tftp-hpa-0.11.tar.gz', file_handler.write())
    file_handler.close()
    ftp_client.quit()

if __name__ == '__main__':
    ftp_file_download(path=FTP_SERVER_URL, username='anonymous', email='nobody@nourl.com')
    
