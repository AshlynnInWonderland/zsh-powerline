# encoding: utf-8
# from config import loadCfg

# config = loadCfg()

def fmtColor(color, bold=False, fg=True):
    if bold:
        strBold = '${fg_bold}'
    else:
        strBold = '${fg_no_bold}'

    if fg:
        strColor = '38;5;'
    else:
        strColor = '48;5;'
    
    return '%{' + '${esc}' + strBold + strColor + str(color) + 'm%}'

# TODO: implement transparent background and alt_lsep
# TODO: implement rprompt (ugh)
def fmtZsh(lprompt=[], rprompt=[]):
    promptText = ''
    first = True
    lastColor = ''
    arrow = ''
    for prompt in lprompt:
        promptText += fmtColor(prompt['bg'], bold=prompt['bold'], fg=False)
        if not first:
            promptText += fmtColor(lastColor, bold=prompt['bold'], fg=True)
            promptText += arrow
        else:
            first = False
        lastColor = prompt['bg']
        promptText += fmtColor(prompt['fg'], bold=prompt['bold'], fg=True)
        if not prompt['text'] == '':
            promptText += ' ' + prompt['text'] + ' '
    promptText += '${reset_color}'
    promptText += fmtColor(lastColor, bold=prompt['bold'], fg=True)
    promptText += arrow
    promptText += '${reset_color}%b '
    return 'local esc=$\'' + chr(27) + '\[\'\n' + 'PROMPT="' + promptText + '"'

if __name__ == '__main__':
    print fmtZsh(lprompt=[{"text":"ASHLYNN","bg":50,"fg":30,"bold":True},{"text":"git","bg":30,"fg":50,"bold":False},{"text":"larry","bg":80,"fg":0,"bold":False}])
