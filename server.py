import socket                   # Import socket module
import pyperclip

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    # print('Server received', repr(data))
    serverdo = 2
    # if data == "GET".encode():
        # print('Client sent message: GET')
        # serverdo = 1
    # else:
        # print('Client sent message: SEND')
        # serverdo = 2
    
    if serverdo == 1:
        filename='mytext.txt'
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
            conn.send(l)
            # print('Sent '+ repr(l))
            l = f.read(1024)
        f.close()
        print('Done sending')
    elif serverdo == 2:
        print('Receiving file')
        open('received_file', 'w').close()
        with open('received_file', 'wb') as f:
            print('file opened')
            while (data):
                print('receiving data...')
                f.write(data)
                data = conn.recv(1024)
            f.close()
        print('copying file to clipboard...')
        g = open('received_file', 'rb')
        copytoclip = g.read().decode('UTF-8', 'ignore')
        print('appending to clipboard:' + copytoclip)
        try:
            pyperclip.copy(copytoclip)
        except:
            print('no clipboard capibility found')
    

    # message = 'Thank you for connecting'
    # conn.send(message.encode())
    conn.close()