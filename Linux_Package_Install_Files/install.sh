dpkg-source -x sherlock_0.14.3+git20240315.55c680f-1.dsc
pip3 install -r sherlock-0.14.3+git20240315.55c680f/requirements.txt
sudo apt-get build-dep sherlock-0.14.3+git20240315.55c680f
cd sherlock-0.14.3+git20240315.55c680f
dpkg-buildpackage -rfakeroot -uc -us
cd ..
sudo dpkg -i sherlock_0.14.3+git20240315.55c680f-1_all.deb
