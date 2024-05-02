# Team 3 CECS 378 Semester Project: Sherlock on Kali Linux Purple

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

### Overview of functionalities our team added:

- Wordlist generation
- Full name lookup capabilities
- Reverse Image Searching

## Getting Started

Instructions for setting up the project locally. Include prerequisites and installation steps.

### Prerequisites

John the Ripper is recommended to use for password cracking with the provided wordlist, but the generated wordlist can be used alone as well.

#### ** Disclaimer ** 

This Linux Package is intended for Debian-based distributions and has only been tested on Kali Linux Purple.

The Sherlock script can be run within any python environment as long as the requirements are installed.
```
pip install -r requirements.txt
```
Python should be able to run sherlock and any of its commands (including the ones added by us) directly from the root directory of this project.

## How to install:

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

Once the project is installed, you can utilize it for data reconnaissance and password cracking as follows:

Run Sherlock: Execute Sherlock to scrape URLs related to your target and generate a wordlist directly.

```
sherlock <username> --wordlist 
```

Password Cracking with John the Ripper: After generating the wordlist, enhance John the Ripper's capabilities for cracking password hashes by providing it with the generated wordlist.

```
john --wordlist=<wordlist> <hash_file>
```

Replace <wordlist> with the path to the generated wordlist file and <hash_file> with the file containing the password hashes you want to crack.

#### Additional Options:

Full Name Search: Perform a search based on the target's full name using the -ns option followed by the target's full name.

```
sherlock -ns <target_full_name>
```

Image Search: Perform a search by image using the -ris option followed by the path to the image file. You must also need to specify a SerpApi key using the -sk option and an Imgur Client ID using the -cid option.

```
sherlock -ris /path/to/image -sk <SerpApi key> -cid <Imgur Client ID>
```

## Lisence

MIT © Sherlock Project
