# WEATHER_STATION_RASPBERRY_PI
Creation d'une station meteo holographique avec raspberry pi
![EfYkw2PWoAA6QKd0](https://user-images.githubusercontent.com/16896722/126657732-928ad382-839a-42b5-8afc-008dde563ecd.jpeg)

TART INSTALLATION


INSTALL SCREEN MHS35

sudo rm -rf LCD-show
sudo git clone https://github.com/goodtft/LCD-show.git
sudo chmod -R 755 LCD-show
cd LCD-show
sudo ./MHS35-show

INSTALL VISUAL STUDIO CODE (OPTIONNAL)

wget https://packagecloud.io/headmelted/codebuilds/gpgkey -O - | sudo apt-key add -
curl -L https://raw.githubusercontent.com/headmelted/codebuilds/master/docs/installers/apt.sh | sudo bash

INSTALL LIBRARY 

sudo apt-get install python3-tk
pip3 install pytz
pip3 install schedule

CLONE REPOSITORY

Mkdir GITHUB
cd GITHUB
git clone https://github.com/juliennoe/Wheater_Station_pi.git

START SCRIPT

cd GITHUB/Wheater_Station_pi/MainProject/REF_SCRIPTS
python3 MainScriptWheater.py

UPDATE / UPGRADE linux

sudo apt-get update
sudo apt-get upgrade

