import os
import sys

def getVerification():

    print 'Initialize "' + os.getcwd() + '" as a code project?'
    while(True):
        c = raw_input('Please enter "(y)es" or "(n)o": ')
        if (c.lower() in ['yes','y']):
            return True
        if (c.lower() in ['no','n']):
            return False

def getProjectType():

    print 'Please select project type, or enter "(q)uit": '
    print '    1) C'
    print '    2) C++'
    print '    3) Java'

    while(True):
        c = raw_input('Project type: ')
        if (c.lower() in ['q', 'quit']):
            return None
        elif (c.lower() in ['c', '1']):
            return 'c'
        elif (c.lower() in ['c++', '2']):
            return 'c++'
        elif (c.lower() in ['java', '3']):
            return 'java'

if (getVerification()):

    projectType = getProjectType()

    if (projectType == 'c'):
        os.system('cp -r ' + sys.argv[0] + '/c/* .')
        pass
    elif (projectType == 'c++'):
        os.system('cp -r ' + sys.argv[0] + '/c++/* .')
    elif (projectType == 'java'):
        os.system('cp -r ' + sys.argv[0] + '/java/* .')
