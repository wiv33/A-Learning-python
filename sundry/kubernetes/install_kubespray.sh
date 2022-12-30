#!/bin/zsh
sudo su

apt install python3.10 python3-pip -y
update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
update-alternatives --config python