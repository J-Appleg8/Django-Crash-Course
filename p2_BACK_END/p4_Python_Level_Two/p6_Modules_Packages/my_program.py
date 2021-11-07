# ##############################################################################################
# Importing function from other Python File ####################################################

####################################################################
# Example 1: Import Whole Module
#
# Since we are in the same folder as the module file, we can just call by the file name
# when this is run, a __pycache__ file shows up in the projects folder
# Its optimized byte code compiled versions of your program's file
# Makes your program start a little faster next time its run
import my_module

my_module.func_in_mymodule()


####################################################################
# Example 2:
import my_module as mm

mm.func_in_mymodule()


####################################################################
# Example 3:
#
# Importing specific functions from Module instead of entire module
from my_module import func_in_mymodule

func_in_mymodule()


####################################################################
# Example 4:
#
# This is posisble but frowned upon, often causes poorly readable code because
# you don't know what functions come from mymodule

from my_module import *

func_in_mymodule()
