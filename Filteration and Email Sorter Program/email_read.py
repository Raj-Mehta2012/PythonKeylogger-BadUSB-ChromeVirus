#coded by Raj Mehta & Vatsal Sharma 
#dated 11 Nov 2020

import re

#change the filename according to ur file
file1 = open('read.txt', 'r') 

Lines = file1.readlines() 
for line in Lines:
    ab = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line)
    print(ab)

