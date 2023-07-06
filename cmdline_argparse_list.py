# USAGE: 
# cmdline_argparse_list.py fname.1 fname.2 fname.3 ...
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='*')
args = parser.parse_args()

for f in args.files:
    print (f)
