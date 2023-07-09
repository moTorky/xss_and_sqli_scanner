import os
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import pickle #used to dump data from memory to files
import argparse #parse user args
from req import req
import subprocess

#test this script
# file_path=dir_name+'/requests_list.pkl'
# with open(file_path, "rb") as file:
# 	loaded_requests_list = pickle.load(file)

# headers_file = 	'header.txt' 
# xsstrike_path=os.path.join("XSStrike/xsstrike.py")
# # Read headers from file
# headers = {}
# with open(headers_file, "r") as f:
#     for line in f:
#         key, value = line.strip().split(":")
#         headers[key.strip()] = value.strip()


# with open('xss_log_file','w') as file:
#     file.write("xsstrike logs")
# Define the command and arguments for xsstrike.py


def xss_scan(loaded_requests_list, headers_file, xsstrike_path, log_file):
# Define common xsstrike command arguments
    xsstrike_common_args = ["--headers", headers_file, "--log-file", log_file,"--file-log-level", "CRITICAL"]

# Loop over the requests list
    for request in loaded_requests_list:
        p = ''
        for param in request.params:
            p += str(param) + "=mrt&"
        if request.method.upper()== 'GET':
            xsstrike_args = [
            "-u",
            request.url + '?' + p]
        else:
            xsstrike_args = [
            "-u",
            request.url, "--data", p]
        # Run xsstrike.py with the specified arguments for the current request
        print('-----------------------------------------------------------')
        print('start to scan: ',request.url,'using',request.method,'method and param:',p)
        print('-----------------------------------------------------------')

        subprocess.run(["python3", xsstrike_path] + xsstrike_common_args + xsstrike_args)
