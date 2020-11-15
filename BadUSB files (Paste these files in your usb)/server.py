#coded by Raj Mehta & Vatsal Sharma 
#dated 11 Nov 2020

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(1)
print(host)
print("Waiting for Connections.......")
conn, addr = s.accept()
print(addr, "Connection to the server Successful.....")

#dont change filename here
filename = 'log.txt'
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Sent Successfully")
