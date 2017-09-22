yum install -y git

if [ ! -d /git ]; then
    mkdir /git
fi

git config --global user.email "da860610@gmail.com"
git config --global user.name "Davis Lin"
git config --global push.default matching
