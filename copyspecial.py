#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Gabby"

import re
import os
import sys
import shutil
import subprocess
import argparse
import zipfile


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # abs_path = []
    # for file in dirname:
    #     os.walk(dirname)
    #     file_path = os.getcwd(file)
    #     if '__' in file_path:
    #         abs_path.append(os.path.abspath(file_path))

    result = []
    for root, dirs, files in os.walk(os.path.abspath(dirname)):
        for name in files:
            if re.findall(r'__(\w+)__', name):
                result.append(os.path.join(root, name))
        break
    return result
    # paths = os.listdir(path)
    # print(paths)
    # for filename in dirname:
    #     if not paths:
    #         path_.append(filename)
    # print(path_)
    # for file in path_:
    #     abs_path.append(os.path.abspath(file))
    # print(abs_path)
    # return abs_path


def copy_to(path_list, dest_dir):
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy(path, dest_dir)

    


def zip_to(path_list, dest_zip):
    compressed = list()
    for path in path_list:
        # compressed.append(zip(path, dest_zip))
    # subprocess.call('zip', len(path_list),  compressed, dest_zip)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
