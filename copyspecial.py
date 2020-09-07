#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Gabby, got help from Sondos and Shanquel"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    result = list()
    for f in os.listdir(dirname):
        if re.search(r'__(\w+)__', f):
            result.append(os.path.abspath(os.path.join(dirname, f)))
    return result


def copy_to(path_list, dest_dir):
    ''' copy file to folder if it the folder does not exist create a file'''
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy(path, dest_dir)


def zip_to(path_list, dest_zip):
    ''' zip from one file to another'''
    subprocess.run(['zip', '-j', dest_zip] + path_list)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='source to read from')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.
    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    special_list = get_special_paths(ns.fromdir)
    if ns.todir:
        copy_to(special_list, ns.todir)
    if ns.tozip:
        zip_to(special_list, ns.tozip)
    print('\n'.join(special_list))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: python copyspecial.py file-to-copy')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
