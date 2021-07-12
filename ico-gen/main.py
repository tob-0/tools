#!/usr/bin/env python3

from PIL import Image
from sys import argv
from pathlib import Path
from os import path

import sys

SCRIPT_NAME = path.basename(__file__)

def help() -> None:
    print(
    f"""Usage: {SCRIPT_NAME} <file_name> [-s <sizes>]

    file_name       The filename or path for the base image.

    -s          A list of the sizes, separated by commas
                Those sizes can be 16, 24, 32, 64, 128.
        
Example:
    {SCRIPT_NAME} logo.png 16,24,32
        Generates logo_16.ico, logo_24.ico and 
        logo_32.ico files.
    {SCRIPT_NAME} logo,png
        Generates a .ico file of each size, from 16 to 128.

A folder named after the input file will be generated for 
the .ico files to be put in.""")
    sys.exit(0)

def main(filepath: str,ico_sizes="16,24,32,64,128") -> None:

    s_name = path.basename(filepath).split('.')[0]
    s_ico_dir = f'./ico-files/{s_name}/'
    s_ext = '.ico'
    Path(s_ico_dir).mkdir(exist_ok=True)

    l_sizes = map(int,ico_sizes.split(','))
    img = Image.open(filepath)

    for size in l_sizes:
        s_suffix='_'+str(size)
        img.save(s_ico_dir + s_name + s_suffix + s_ext,sizes=[(size,size)])
    
    

    sys.exit(0)

if len(argv) < 2:
    print(f"Usage: {SCRIPT_NAME} <file_name> [-s <sizes>]")
    sys.exit(-1)
elif (('-h' in argv) or ('--help' in argv)):
    help()
else:
    for i,arg in enumerate(argv):
        if arg == '-s':
            if not argv[i+1] :
                print("You must provide sizes with the -s flag.")
                sys.exit(-2)
            else: main(argv[1],argv[i+1])
        elif arg not in ['-s','-h','--help',__file__]:

            if i == 1: continue

            print(f"Unrecognized flag '{arg}' ")
            print(f"Usage: {SCRIPT_NAME} <file_name> [-s <sizes>]")
            sys.exit(-3)
    main(argv[1])