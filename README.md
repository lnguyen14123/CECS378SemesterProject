<<<<<<< HEAD

# Team 3 CECS 378 Semester Project

Brief description of the project.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

Brief introduction or overview of the project. Provide context about its purpose and goals.

## Features

- Feature 1
- Feature 2
- ...

## Getting Started

Instructions for setting up the project locally. Include prerequisites and installation steps.

### Prerequisites

List any software, tools, or dependencies required to run the project.

## How to install:

### Step 1. add a deb-src to sources.list if not done already
####change permissions of sources.list so you may write to file
```
sudo chmod 777 /etc/apt/sources.list
```

#### edit with your editor of choice
```
vi /etc/apt/sources.list
```
#uncomment the line that begins with deb-src -> esc -> :wq

#### restore permissions to file
```
sudo chmod 644 /etc/apt/sources.list
```

### Step 2. run the install.sh file 
##### Change directory to where install.sh is located CECS378SemesterProject/Linux_Package_Install_Files/

```
cd CECS378SemesterProject/Linux_Package_Install_Files/
```

##### make the file executable
```
chmod +x install.sh
```
##### run the shell file and respond to prompts
```

./install.sh
```
