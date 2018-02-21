# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:34:39 2017

@author: Administrator
"""

import os

path = r"C:\OOP\prank"
saved_path = os.getcwd()
print "Current working directory is " + saved_path
os.chdir(path)
def rename_files():
    # get file names from a folder
    file_list = os.listdir(path)
    
    # for each file, rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"1234567890"))

rename_files()