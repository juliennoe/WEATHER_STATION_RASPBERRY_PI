INSTALL SCREEN MHS35

sudo rm -rf LCD-show
sudo git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show
sudo ./MHS35-show

INSTALL VISUAL STUDIO CODE (OPTIONNAL)

wget https://packagecloud.io/headmelted/codebuilds/gpgkey -O - | sudo apt-key add -

curl -L https://raw.githubusercontent.com/headmelted/codebuilds/master/docs/installers/apt.sh | sudo bash

UPDATE / UPGRADE linux

sudo apt-get install python3-tk
pip3 install pytz
pip3 install schedule

CLONE REPOSITORY

Mkdir GITHUB
cd GITHUB
git clone https://github.com/juliennoe/openImagePython.git
cd GITHUB/openImagePython/test
git clone https://github.com/mchobby/lcdmtrx.git
mettre image.py dans dossier lcdmtrx
mettre clean_screen.py dans dossier lcdmtrx
python3 image.py