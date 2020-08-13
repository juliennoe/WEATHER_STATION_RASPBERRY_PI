{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red84\green36\blue84;
\red172\green172\blue169;\red27\green30\blue31;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c99926\c0;\cssrgb\c40588\c20588\c40384;
\cssrgb\c73161\c73155\c72035;\cssrgb\c14248\c15434\c16112;}
\paperw11900\paperh16840\margl1440\margr1440\vieww9880\viewh15780\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf2 \cb3 INSTALL SCREEN MHS35\
\
\pard\pardeftab720\sl364\partightenfactor0

\f1\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 sudo rm -rf LCD-show\
git clone {\field{\*\fldinst{HYPERLINK "https://github.com/goodtft/LCD-show.git"}}{\fldrslt \cb3 \strokec4 https://github.com/goodtft/LCD-show.git}}\
chmod -R 755 LCD-show\
cd LCD-show/\
sudo ./MHS35-show\
\

\f0\fs24 \cb3 INSTALL VISUAL STUDIO CODE (OPTIONNAL)\
\
\pard\pardeftab720\partightenfactor0

\f1\fs28 \cf2 \cb3 \strokec5 wget https://packagecloud.io/headmelted/codebuilds/gpgkey -O - | sudo apt-key add -\cb3 \strokec2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec5 curl -L https://raw.githubusercontent.com/headmelted/codebuilds/master/docs/installers/apt.sh | sudo bash\
\
\pard\pardeftab720\sl364\partightenfactor0

\f0\fs24 \cf2 \cb3 \outl0\strokewidth0 UPDATE / UPGRADE linux\
\

\f1\fs28 \cb3 sudo apt-get update\
Sudo apt-get upgrade\
\cb3 \outl0\strokewidth0 \strokec5 \
\pard\pardeftab720\sl364\partightenfactor0

\f0\fs24 \cf2 \cb3 \outl0\strokewidth0 INSTALL LIBRARY PYTHON\
\
\pard\pardeftab720\partightenfactor0

\f1\fs28 \cf2 \cb3 \outl0\strokewidth0 \strokec6 sudo apt-get install python3-tk
\f0\fs24 \cb3 \outl0\strokewidth0 \
\pard\pardeftab720\sl364\partightenfactor0

\f1\fs28 \cf2 \cb3 pip3 install pytz\
pip3 install schedule\
\

\f0\fs24 \cb3 CLONE REPOSITORY\
\

\f1\fs28 \cb3 Mkdir GITHUB\
cd GITHUB\
git clone https://github.com/juliennoe/openImagePython.git\
cd GITHUB/openImagePython/test\
python3 image.py}