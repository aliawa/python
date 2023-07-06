import argparse

# Program description
parser = argparse.ArgumentParser(description="calculate X to the power of Y")

# Positional arguments. These are mandatory
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

# Optional argument, string
parser.add_argument("-s", "--string", help="the string argument")

# Optional argument, integer
parser.add_argument("-i", "--integer", type=int, help="the integer argument")

# Flag options, true when option is present false otherwise.
parser.add_argument("-f", "--flag", action="store_true")

# Flag with a const value
parser.add_argument("--cflag", action="store_const", const="42")

# Choice
parser.add_argument("--choice", type=int, choices=[1,2,3], help="chose 1,2 or 3")

# How many times the option was specified
parser.add_argument("-r", "--repeated", action="count", default=0)

# Mutually exclusive group. Only one option from the group is allowed.
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

# if --sum is specifed args.accumalate will be sum otherwise it 
# will be max
parser.add_argument('integers', metavar='N', type=int, nargs='+',
        help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
        const=sum, default=max,
        help='sum the integers (default: find the max)')

args = parser.parse_args()
answer = args.x**args.y


def main():
    if args.quiet:
        print (answer)
    elif args.verbose:
        print ("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        print ("{}^{} == {}".format(args.x, args.y, answer))

    print ("string arg was: {}".format(args.string))
    print ("integer arg was: {}".format(args.integer))
    print ("r was repeated: {} times".format(args.repeated))

    print ("accumulate: {}".format(args.accumulate(args.integers)))
    print ("choice is {}".format(args.choice))
    print ("cflag is {}".format(args.cflag))


if __name__ == "__main__":
    main()
