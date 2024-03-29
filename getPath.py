import os

# Returns the path to <target> if it's in the current directory or
# in any ancestor directories of <directory>, otherwise returns None
def getPath(directory, target):
    while (directory != ''):
        if target in [item for item in os.listdir(directory)]:
            return directory + '/' + target
        directory = directory[:directory.rfind('/')]
