import sys

print ()
print ("number of args recevied: {}".format(len(sys.argv)))

for i, arg in enumerate(sys.argv):
    print ("sys.argv[{}] ='{}'".format(i, arg))


