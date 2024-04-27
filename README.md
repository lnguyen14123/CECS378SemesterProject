<<<<<<< HEAD

# Team 3 CECS 378 Semester Project

An expansion of Sherlock's data reconnaisance capabilities.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Usage](#usage)
4. [License](#license)

## Introduction

By utilizing a mix of John the Ripper as well as Sherlock, this project combines the abilities of data reconnaissance and password cracking in order to expand the capabilities of John the Ripper. By webscraping URLs provided by Sherlock for any one target, a wordlist can be produced with passwords potentially used by the target. Then, by providing this wordlist to John the Ripper, John can better crack password hashes generated from the target user.

## Getting Started

Instructions for setting up the project locally. Include prerequisites and installation steps.

### Prerequisites

John the Ripper is recommended to use for password cracking with the provided wordlist, but the generated wordlist can be used alone as well.

## How to install:

### Step 1. add a deb-src to sources.list if not done already
#### change permissions of sources.list so you may write to file
```
sudo chmod 777 /etc/apt/sources.list
```

#### edit with your editor of choice
```
vi /etc/apt/sources.list
```
#### uncomment the line that begins with deb-src -> esc -> :wq

#### restore permissions to file
```
sudo chmod 644 /etc/apt/sources.list
```

### Step 2. run the install.sh file 
#### Change directory to where install.sh is located CECS378SemesterProject/Linux_Package_Install_Files/

```
cd CECS378SemesterProject/Linux_Package_Install_Files/
```

#### make the file executable
```
chmod +x install.sh
```
#### run the shell file and respond to prompts
```

./install.sh
```

## Usage
to be finished

## Lisence

MIT © Sherlock Project
