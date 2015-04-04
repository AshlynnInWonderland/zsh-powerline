mkdir ~/.zsh-powerline
git clone https://github.com/AshlynnInWonderland/zsh-powerline.git ~/.zsh-powerline/zsh-powerline
cp -r ~/.zsh-powerline/zsh-powerline/default/* ~/.zsh-powerline
cp ~/.zsh-powerline/zsh-powerline/zline.sh ~/.zsh-powerline
echo "Add the following like to your .zshrc to finish installing:\nsource ~/.zsh-powerline/zline.sh"
