import os
import sys
from getPath import getPath

# The directory containing the binary
binDir = 'bin'

# Couldn't find the bin directory
binDirPath = getPath(os.getcwd(), binDir)
if binDirPath is None:
    print ('Could not find "bin" directory anywhere in the path of ' + os.getcwd())
    sys.exit()

# Couldn't find any valid binaries
binary = next((x for x in os.listdir(binDirPath) if '.fuse_hudden' not in x), None)
if binary is None: 
    print ('Could not find any valid binaries in the folder "' + binDirPath + '"')
    sys.exit()

# Replace ' ' with '\ ' in the path to the binary
command = (binDirPath + '/' + binary).replace(' ', '\\ ')

# Exclude this script from the arguments to the binary
args = sys.argv[1:]

# Check for valgrind
if 0 < len(args) and args[0] == 'valgrind':
    command = 'valgrind ' + command
    args = args[1:]

# Execute the command with the args we provided to this script
os.system(command + ' ' + ' '.join(args))
