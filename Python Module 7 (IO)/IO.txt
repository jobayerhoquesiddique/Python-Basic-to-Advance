"""File I/O"""

#Create a new file "practice.txt" using python.Add the following data in it
#Hi Everyone
#we are learning File I/O
#Using Java 
#I like programming in Java

with open("Practice.txt","w") as f:

    f.write("Hi Everyone \nwe are learning File I/O Using Java")
    f.write("\nI like programming in Java")
#Lets Read a file 
f= open("Practice.txt","r")
data=f.read(5)
line1=f.readline()
print(line1)
line3=f.readline()
print(line3)
print(type(data))
f.close()
"""Let's Write File"""
#write/overwrite
#append
#Create
with open("Sample.txt",'w') as f:
    f.write("I don't know how I don't know why")

with open("Sample.txt","w") as f:
    f.write("\nThis is not working")
    
#Delete a file 
import os
os.remove("Practice.txt")
    
"""File I/O and Error Handling"""
#From Shohoj Bhashay Python 3 by Maksudur Rahman Mateen 
"""File"""

my_file = open("test.txt","r")
content = my_file.read()
print(content)
my_file.close()


my_file = open("test.txt","w")
my_file.write("I am Jobayer Hoque Siddique")
my_file.close()

"""Error Handling"""
#try except feature
try:
    with open("test.txt","r") as my_file:
     content = my_file.read()
    print(content)
except:
    print("This file does not exist")
    print("Made by Jobayer")

try:
    my_file = open("test.txt")
    content=my_file.read()
    i=int(content.strip())
except IOError as e:
    errno,strerror=e.args
    print("I/O error({0}):{1}".format(errno,strerror))
except ValueError:
    print("No valid int in the line.")
except:
    print("Unexpected error!")

#alt
try:
    my_file=open("test.txt")
    content=my_file.read()
    i=int(content.split())
except (IOError,ValueError):
    pass
