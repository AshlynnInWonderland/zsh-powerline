# encoding: utf-8
import imp

import config
from formatting import fmtZsh

def loadModule(name, path):
    module = imp.load_source(name, path)
    if hasattr(module, "returnText"):
        return module.returnText()
    else:
        return "module not found"

def loadAll():
    modules = config.listModules()
    cfg = config.loadCfg()
    for obj in cfg['lprompt']:
        try:
            modpath = modules[obj['module']]
            obj['text'] = loadModule(obj['module'], modpath)
        except:
            obj['text'] = ''
    shelfmodpath = modules[cfg['shelf']['module']]
    cfg['shelf']['text'] = loadModule(cfg['shelf']['module'], shelfmodpath)
    return cfg

if __name__ == '__main__':
    finCfg = loadAll()
    print(fmtZsh(lprompt=finCfg['lprompt'],shelf=finCfg['shelf']))
