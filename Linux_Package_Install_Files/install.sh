sudo apt update
dpkg-source -x sherlock_0.14.3+git20240315.55c680f-1.dsc
cd sherlock-0.14.3+git20240315.55c680f
sudo apt-get build-dep .
pip3 install -r requirements.txt
dpkg-buildpackage -rfakeroot -uc -us
cd ..
sudo dpkg -i sherlock_0.14.3+git20240315.55c680f-1_all.deb
