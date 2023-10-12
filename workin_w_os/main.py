import argparse
import os 
import shutil
import sys

DATASET_DIR = 'dataset'

parser = argparse.ArgumentParser()
dir_help = 'a directory of source files, defaults to directory'
parser.add_argument('-d', '--directory', default='directory', help=dir_help)
ext_help = 'an extension for looking files up, defaults png'
parser.add_argument('-e', '--extension', default='png', help=ext_help)
args = parser.parse_args(sys.argv[1:])

if not os.path.isdir(args.directory):
    print(f'{args.directory} is not a directory')
    exit(1)

if not os.path.isdir(DATASET_DIR):
    print(f'{DATASET_DIR} is not a directory, creating')
    os.mkdir(DATASET_DIR)

def full_name(file: str):
    return os.path.join(args.directory, file)

def is_wanted(file: str):
    return os.path.isfile(full_name) and ('.' in file and file.split('.')[-1] == args.extension)

files = list(filter(is_wanted, os.listdir(args.directory)))

index = 1

for index, file in enumerate(sorted(files)):
    old, new = full_name(file), os.path.join(DATASET_DIR, f'{index+1}.{args.extension}')
    shutil.copy(old, new)
    print(f'{old} was copied {new}.')
