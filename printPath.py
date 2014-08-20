import os
import sys
from getPath import getPath

if (1 < len(sys.argv)):
    print getPath(os.getcwd(), sys.argv[1])
