# encoding: utf-8
from os import getcwd
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

# TODO: implement transparent background and alt_lsep (messy) - cannot fix willnot fix
# TODO: implement rprompt (tiring)
def fmtZsh(lprompt=[], rprompt=[], shelf={}):
    promptText = ''
    first = True
    lastColor = ''
    arrow = ''
    altArrow = ''
    # build main body of prompt
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
    # reset background and add trailing arrow
    promptText += '${reset_color}'
    promptText += fmtColor(lastColor, bold=prompt['bold'], fg=True)
    promptText += arrow
    # shelf 
    if shelf:
        promptText += fmtColor(shelf['fg'], bold=shelf['bold'], fg=True)
        if not shelf['text'] == '':
            promptText += ' ' + shelf['text'] + ' '
        else:
            promptText += shelf['text']
        promptText += altArrow
    # reset color and boldness
    promptText += '${reset_color}%b '
    return 'local esc=$\'' + chr(27) + '\[\'\n' + 'PROMPT="' + promptText + '"'

# Testing
if __name__ == '__main__':
    print fmtZsh(lprompt=[
        {
            "text":"ASHLYNN",
            "bg":190,
            "fg":17,
            "bold":True
        },
        {
            "text":" master",
            "bg":238,
            "fg":255,
            "bold":False
        }
    ],
    shelf={
        "text":getcwd(),
        "fg":85,
        "bold":False
    })
