# Installation Guide for Criminality UK

## Install ptyhon

To run the project you need to install python. The version needs to be 3.0.0 or higher but not higher than 3.8.*

Dowloads for windows: https://www.python.org/downloads/windows/ 
Downloads for macos: https://www.python.org/downloads/macos/ 
other: https://www.python.org/download/other/ 

Recommended version: 3.8.10

**Important:** make sure pip is installed and enviromental variabel is set!

check installation in terminal:
- python -V
- pip -V


## Install libraries

Additionally you have to install some libraries to not get any errors. To do so, follow these steps:

1. open a terminal
2. install libraries with command lines:
	- pip install requests
	- python -m pip install -U matplotlib
	- pip install numpy
	- pip install pysimplegui
	

## Run

1. open a terminal
2. locate the project on your machine
3. go to src/app/gui and enter:
	- python gui.py
