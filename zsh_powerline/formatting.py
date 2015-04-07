# encoding: utf-8
from os import getcwd
from config import loadCfg

def fmtColor(color, bold=False, fg=True, first=False, wlb=False):
    if first and bold:
        strBold = '${fg_bold}'
    elif first and wlb:
        strBold = '${fg_no_bold}'
    else:
        strBold = ''

    if fg:
        strColor = '38;5;'
    else:
        strColor = '48;5;'
    
    return '%{' + '${esc}' + strBold + strColor + str(color) + 'm%}'

# TODO: implement rprompt (tiring)
def fmtZsh(lprompt=[], rprompt=[], shelf={}, errors=[]):
    promptText = ''
    first = True
    lastColor = ''
    wasLastBold = False
    arrow = ''
    altArrow = ''
    # build main body of prompt
    if lprompt:
        for prompt in lprompt:
            promptText += fmtColor(prompt['bg'], bold=prompt['bold'], fg=False)
            if not first:
                promptText += fmtColor(lastColor, bold=prompt['bold'], fg=True)
                promptText += arrow
            else:
                first = False
            lastColor = prompt['bg']
            promptText += fmtColor(prompt['fg'], bold=prompt['bold'], fg=True, first=True, wlb=wasLastBold)
            wasLastBold = prompt['bold']
            if not prompt['text'] == '':
                promptText += ' ' + prompt['text'] + ' '
        # reset background and add trailing arrow
        promptText += '%{${esc}0m%}'
        promptText += fmtColor(lastColor, bold=prompt['bold'], fg=True)
        promptText += arrow
    # shelf 
    if shelf:
        promptText += fmtColor(shelf['fg'], bold=shelf['bold'], fg=True, first=True, wlb=wasLastBold)
        if not shelf['text'] == '':
            promptText += ' ' + shelf['text'] + ' '
        else:
            promptText += shelf['text']
        promptText += altArrow
    # reset color and boldness
    promptText += '%{${esc}0m%} '
    rtnString = 'local esc=$\'' + chr(27) + '\[\'\n' + 'PROMPT="' + promptText + '"'
    for error in errors:
        rtnString += '\n' + error
    return rtnString

# Testing
if __name__ == '__main__':
    cfg = loadCfg()
    print(fmtZsh(lprompt=cfg['lprompt'],shelf=cfg['shelf']))
    # print(fmtZsh(lprompt=[
    #     {
    #         "text":"ASHLYNN",
    #         "bg":190,
    #         "fg":17,
    #         "bold":True
    #     },
    #     {
    #         "text":" master",
    #         "bg":238,
    #         "fg":255,
    #         "bold":False
    #     }
    # ],
    # shelf={
    #     "text":getcwd(),
    #     "fg":85,
    #     "bold":False
    # }))
