import argparse

# you can call this program as:
# python sample_argparse.py --sum 1 2 3
# python sample_argparse.py 1 2 3


# Step1: create "ArugumentParser" object 
# Text to display before help is "Proces some integers"
parser = argparse.ArgumentParser(description='Process some integers.')


# Step2: Filling the ArgumentParser with information about program arguments

# integers is positional because it does not have "-" or "--"
# nargs='+', gather all positional command line args into a list
# type=int, by default command line args are strings.
# metavar='N', print as 'N' in help
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

# optional arg because it starts with "--"
# dest='accumulate', the name of the attribute added by parse_args is 'accumulate'
#    and not 'sum'
# const=sum, default=max, when --sum is present sum is assigend to obj.accumulate
#    otherwise max is added by default
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

# Convert argument strings to objects and assign them as attributes of the 
# namespace. Return the populated namespace.
args = parser.parse_args()


# Step 3: Use the object returned by parse_args()
# Since we made parse_args assign 'sum' or 'max' to '.accumulate', which are 
# python built in fuctions, so args.accumulate is acually a callable
# and args.integers is a list because we said 'nargs='+'
print(args.accumulate(args.integers))
