#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:31:37 2018

@author: michaelcasper
"""

# selectiveCopy.py - Walks through a folder tree and searches for files
# with a certain file extension.
# Copies these files from where there were into a new folder.
# Call selective_copy(search_folder, extension, destination_folder)
# to run program. Destination folder should not exist yet; it will be created.

import re
import shutil
import os


# Use a regular expression to search for files with a specified exension.
def does_match_extension(filename, extension):
    extension_regex = re.compile('{0}$'.format(extension))
    match = extension_regex.search(filename)
    if match is None:
        return False
    else:
        return True


# Walk through the specified folder tree.
def folder_walk(search_folder, extension, destination_folder):
    for foldername, subfolders, filenames in os.walk(search_folder):
        if os.path.abspath(foldername) == os.path.abspath(destination_folder):
                continue
        for filename in filenames:
            if foldername == destination_folder:
                continue
            if does_match_extension(filename, extension) is True:
                shutil.copy(os.path.join(foldername, filename),
                            destination_folder)
                print('Adding %s to %s...' % (filename, destination_folder))
            else:
                continue


# Main function to run the program.
def selective_copy(search_folder, extension, destination_folder):
    os.mkdir(os.path.abspath(destination_folder))
    folder_walk(search_folder, extension, destination_folder)
    print('\nDone.')
