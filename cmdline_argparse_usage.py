# USAGE:
# cmdline_argparse_usage.py [-l] <directory name to list>

# Import the argparse library
import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser()

# Add positional argument, access as args.Path
my_parser.add_argument('Path')

# Add optional argument, when this is present args.l is true
my_parser.add_argument('-l', action='store_true')

# Execute parse_args() -- all done with argparse
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

for line in os.listdir(input_path):
    if args.l:  # long listing
        size = os.stat(os.path.join(input_path, line)).st_size
        line = '%10d  %s' % (size, line)
    print(line)

