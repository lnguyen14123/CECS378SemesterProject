How to install:

Step 1. add a deb-src to sources.list if not done already
# change permissions of sources.list so you may write to file
sudo chmod 777 /etc/apt/sources.list

# edit with your editor of choice
vi /etc/apt/sources.list
#uncomment the line that begins with deb-src -> esc -> :wq

# restore permissions to file
sudo chmod 644 /etc/apt/sources.list

Step 2. run the install.sh file 
#Change directory to where install.sh is located CECS378SemesterProject/Linux_Package_Install_Files/
cd CECS378SemesterProject/Linux_Package_Install_Files/

#make the file executable
chmod +x install.sh

#run the shell file and respond to prompts
./install.sh
