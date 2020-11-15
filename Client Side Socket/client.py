#coded by Raj Mehta & Vatsal Sharma 
#dated 11 Nov 2020

import socket

s = socket.socket()
#host = input(str("Pls enter the host Address: "))
host= 'DESKTOP-I073121'
port = 12345
s.connect((host, port))
print("Connection Successful")

#set file name
filename= 'log_received.txt'
file = open(filename, 'wb')
file_data= s.recv(1024)
#print(file_data)
file.write(file_data)
file.close()
print("File Recieved Successfully")
