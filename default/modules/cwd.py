import os

def returnText():
    cwd = os.getcwd().replace(os.environ['HOME'],'~')
    lstCwd = str.split(cwd, '/')
    if len(lstCwd) > 3:
        lstCwd.reverse()
        lstCwd = lstCwd[0:3]
        lstCwd.append('+')
        lstCwd.reverse()
    strCwd = '/'.join(lstCwd)
    return strCwd
