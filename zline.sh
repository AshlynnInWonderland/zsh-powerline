function __zline {
  source <( python3 ~/git/zsh-powerline/zsh_powerline/load.py )
}

if [[ ! ${precmd_functions[(r)__zline]} == __zline ]]; then
  precmd_functions+=(__zline)
fi
