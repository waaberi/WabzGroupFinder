# Wabz Group Finder

This is a group finder for rblx

## Installation

### Needed programs

You need:

1. NodeJS
2. NPM

### Manual Install

1. Clone this repository (or download as ZIP and extract)
2. Change the directory to that repository
3. Run <code>npm install</code> to install the dependencies
4. Create a .env file
   <pre>
   WEBHOOK_URL=Your_webhook_url_here
   MODE=normal
   </pre>
   Normal is the normal mode. Proxy mode is comming soon. Keep in mind that it is case sensitive.
5. Run <code>node index.js</code> to run the code.

You might want to run this with PM2, a guide for this is comming soon.

### Windows Automatic install

Comming soon. I just need to do PyToExe for the installer script.
If you have some bash emulator (CygWin, MinTTY), you can follow the Unix based OSes Automatic Install and it should work, but you also need Python, and make sure to write python instead of python3, because there is no distinction for the executable name in Windows.

### MacOS, Linux, BSD, other Unix based OSes Automatic Install

You need Python3 to run this installer. It is installed on most Unix based OSes by default. You also need the bash shell. It's the default shell for almost all Unix Based OSes.

Run this command on bash on an empty folder: <pre>python3 <(wget https://raw.githubusercontent.com/rblxploit/WabzGroupFinder/master/install.py -q -O-)</pre>

It will tell you the rest.
