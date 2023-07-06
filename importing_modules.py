# import module fibo
# then use as fibo.fib and fibo.fib2
import fibo

# import specific names. In this case fibo is not defined.
# in importing module's symbol table
from fibo import fib, fib2

# import all names that a module defines
# except those starting with an '_'
from fibo import *

# search path for modules
sys.path
environment variable: PYTHONPATH
import sys
sys.path.append('/ufs/guido/lib/python')


# List all names defined in a module.
dir(fibo)

# List currently defined names
dir()

# List names of builtin functions
import builtins
dir(builtins)



# All local variables as a dictionary
vars()



