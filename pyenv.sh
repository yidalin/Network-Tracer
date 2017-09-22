#!/bin/bash

yum install -y sqlite-devel

yum install -y gcc zlib-devel.x86_64 bzip2.x86_64 bzip2-devel.x86_64 readline-devel.x86_64 openssl-devel.x86_64

curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

source ~/.bash_profile

pyenv -v

# pyenv install 2.7.14
pyenv install 3.6.2
