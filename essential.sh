#!/bin/bash
cd $HOME
apt install neovim gh git nethogs wavemon
wget https://download.nomachine.com/download/8.12/Raspberry/nomachine_8.12.12_3_arm64.deb
sudo dpkg -i nomachine_8.12.12_3_arm64.deb
