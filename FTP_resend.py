import sys
import time
import ftplib
import datetime
import os
import random



"""FTP_HOST = "103.9.86.28"
FTP_USER = "tdavuong"
FTP_PASS = "d6uUBzjGXA"
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)

"""

FTP_HOST = "103.126.153.235"
FTP_USER = "XIMANGDONGLAM"
FTP_PASS = "ximangdonglamhue"
upload_dir = "/Test/nglieu/"
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
path = r"C:\Users\ngoma\PycharmProjects\FTP\DATA_test"
ftp_file_name = ftp.nlst()
local_file_name = os.listdir(path)
"""FTP_HOST = "103.164.245.205"
FTP_USER = "siflex"
FTP_PASS = "Siflex@ftp"
upload_dir = "/HN/{D3C6F27F-E84F-4F44-867C-A23BBEECD8E1}/{2E729CC4-64E5-4E77-8C15-5BCDEB763847}/"
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)"""

def directory_exists(dir):
    filelist = []
    ftp.retrlines('LIST', filelist.append)
    for f in filelist:
        if f.split()[-1] == dir and f.upper().startswith('D'):
            return True
    return False
def compare_file():
    i = 0
    for file_name in local_file_name:
        local_file_path = os.path.join(path, file_name)
        if file_name not in ftp_file_name:
            year = file_name[16:20]
            month = file_name[20:22]
            date = file_name[22:24]
            first_dir = upload_dir + year
            second_dir = first_dir + "/" + month
            last_dir = second_dir + "/" + date
            # Create multiple folder in FTP server
            try:
                directory_exists(upload_dir)
                ftp.mkd(upload_dir)
            except ftplib.error_perm:
                pass
            try:
                directory_exists(first_dir)
                ftp.mkd(first_dir)
            except ftplib.error_perm:
                pass
            try:
                directory_exists(second_dir)
                ftp.mkd(second_dir)
            except ftplib.error_perm:
                pass
            try:
                directory_exists(last_dir)
                ftp.mkd(last_dir)
            except ftplib.error_perm:
                pass
            ftp.cwd(last_dir)
            try:
                with open(local_file_path, 'rb') as file:
                    ftp.storbinary(f'STOR {file_name}', file)
                    print(f"File '{file_name}' uploaded successfully.")
                    i+=1
                    print(i)
            except ftplib.error_perm:
                pass

compare_file()
# Testing interval function
