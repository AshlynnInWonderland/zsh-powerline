from json import load
import os

cfgDir = os.path.expanduser('~/.zsh-powerline/')

def loadCfg():
    return load(open(cfgDir + 'config.json', 'r'))

def listModules():
    modules = {}
    for fileName in os.listdir(cfgDir + 'modules/'):
        moduleName, fileExt = os.path.splitext(fileName)
        if fileExt.lower() == '.py':
            modules[moduleName] = cfgDir + 'modules/' + fileName
    return modules

if __name__ == '__main__':
    print(loadCfg())
    print(listModules())
