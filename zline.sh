function __zline {
  source <( python3 ~/.zsh-powerline/zsh-powerline/zsh_powerline/load.py )
}

if [[ ! ${precmd_functions[(r)__zline]} == __zline ]]; then
  precmd_functions+=(__zline)
fi
