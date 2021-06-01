import socket                   # Import socket module
from pynput import keyboard
import tkinter as tk

host = input('Where to connect to (IP can be found through hostname -i on linux, ipconfig -a on windows): ')     # Where to connect to
port = 60000

def getClipboardText():
    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    try:
        return root.clipboard_get().encode("UTF-8", "ignore")
    except:
        return "ERR: clipboard is not text".encode()

def send():
    s = socket.socket()             # Create a socket object
    s.connect((host, port))
    #s.send("SEND".encode())
    
    print('clipboard contains: ' + getClipboardText().decode('UTF-8', 'ignore'))
    g = open('mytext.txt', 'wb')
    g.write(getClipboardText())
    g.close()
    
    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while l != b'':
        s.send(l)
        print('Sent '+ repr(l))
        l = f.read(1024)
    f.close()
    print('Done sending')

def on_activate():
    print('Global hotkey activated!')
    send()

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<alt>+c'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
