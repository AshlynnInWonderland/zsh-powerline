import subprocess as sp

#this code is disgusting and I'm ashamed of it

def returnText():
    return " " + sp.check_output(['git','symbolic-ref','--quiet','HEAD'], stdin=None, stderr=sp.PIPE, shell=False, universal_newlines=False).strip().decode('utf-8').split('/')[2]
