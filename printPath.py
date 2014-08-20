import os
import sys

# Prints the path to <target> if it's the current directory or
# any ancestor directories of <directory>, otherwise prints nothing
def getPath(directory, target):
    while (directory != ''):
        if target in [item for item in os.listdir(directory)]:
            return directory + '/' + target
        directory = directory[:directory.rfind('/')]

# This should never be false, so long as the 'cd.sh' is correct
if (1 < len(sys.argv)):
    print getPath(os.getcwd(), sys.argv[1])
