# PySharedclipboard


## About


This is a set of python scripts to get a shared clipboard between two computers. 


## Usage


Firstly, the packages `pynput` and `pyperclip` are required. For some computers running Linux, installing xclip via `sudo apt-get install xclip` or a similar command such as `sudo pacman -S xclip` based on your distro is required. 


The program consists of a server and a client script, both of which have to be running on both computers in order for it to work. Run `python server.py` and `python client.py` in two seperate terminal windows to get the program started. 


Next, after running the client script, you will be prompted for the IP address of the computer you want to connect to. Keep in mind that this is the local IP address of the target computer, and that the scripts must be run between two computers on LAN. Dialing in the IP of a remote computer on another network will not work.


After that, everything is set up. On one computer, copy some text into your clipboard, then press the keys `alt + c`. This will send what is currently in your keyboard over to the other computer, where it will automatically be copied into its clipboard. On that computer, you can repeat the process to send that computer's clipboard over to the first computer.


