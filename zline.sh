function __zline {
  source <( python2 ~/git/zsh-powerline/zsh_powerline/formatting.py )
}

if [[ ! ${precmd_functions[(r)__zline]} == __zline ]]; then
  precmd_functions+=(__zline)
fi
