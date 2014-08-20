import os
import sys
from getPath import getPath

# The target
makefile = 'Makefile'

# If at first we don't succeed, look for 'makefile' instead
makefilePath = getPath(os.getcwd(), makefile)
if makefilePath is None:
    makefilePath = getPath(os.getcwd(), makefile.lower())

# Now we really couldn't find the makefile
if makefilePath is None:
    print ('Could not find "' + makefile + '" anywhere in the path of ' + os.getcwd())
    sys.exit()

# Extract just the root directory and then run make in that directory
rootDir = makefilePath[:-len('/' + makefile)].replace(' ', '\\ ')

# Ensure this script isn't an argument to the make command
args = sys.argv[1:]

# Run the make commands with the given arguments
os.system('make ' + ' '.join(args) + ' -C ' + rootDir)
