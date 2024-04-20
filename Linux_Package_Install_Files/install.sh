#must update apt after changing deb-src
sudo apt update

#compile the source files for the package
dpkg-source -x sherlock_0.14.3+git20240315.55c680f-1.dsc

#change director to root dir of source files
cd sherlock-0.14.3+git20240315.55c680f

#build dependencies for package as stated in debian/control file
sudo apt-get build-dep .

#install python run-time dependencies
pip3 install -r requirements.txt

#build an unsigned version of the package. along with fakeroot as to not alter system files by accident
dpkg-buildpackage -rfakeroot -uc -us

# return to original dir
cd ..

#install the built package
sudo dpkg -i sherlock_0.14.3+git20240315.55c680f-1_all.deb