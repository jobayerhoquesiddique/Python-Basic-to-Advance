#Second lesson . It's about (Strings,Indexing,String function & Conditional statement) 

"""String"""
#String is a data type that store sequence of character
"Concetination"
#It is use to sum word
'''print("Hello"+"World")'''

"""Length of string"""
#How long is the character
'''pri="Hello"+"World"
print(len(pri))'''

"""Indexing (Slicing/Negative Index)"""
#These are word and their spot_number(known as index)
'''Name="JubuChumuMuzu"
print(Name[0:])
print(Name[1:8])
print(Name[-5:-8])'''

"""String Function"""
ter="joBayda iS bAd"
print(ter.capitalize())
print(ter.title())
print(ter.lower())
print(ter.count("a"))
print(ter.swapcase())
print(ter.split("iS"))
print(ter.isalpha())#false
print(ter.isalnum())
print(ter.replace("bAd","good"))

"""Conditional Statement"""
#if-elif-else
'''Age=21
X=None
Y=None
Z=None
if(Age>=18):
    X="Can drive"
elif(Age<=18):
    Y="Cannot drive"
else:
    Z="Dead"
print(X)
print(Y)
print(Z)'''

"""PRACTICE EXCERCISE"""
#_1 WAP Grade students based on marks?
""" mark >= 90  , grade= "A"
    90 > mark >= 80 , grade = "B"
    80 > mark >= 70 , grade = "C"
    70 > mark,grade="D" """
'''Mark=int(input("Enter Students Mark"))
if(Mark>=90):
    print("A")
elif(Mark<90 and Mark>=80):
    print("B")
elif(Mark<80 and Mark>=70):
    print("C")
elif(Mark<70):
    print("D")'''

#_2 WAP to check if a number entered by the user is odd or even?
'''Number=int(input("Enter Number"))
if(Number%2==0):
    print("Even")
else:
    print("ODD")'''

#_3 WAP to find the greatest of 3 numbers entered by the user?
'''X=float(input("Enter 1st/X number:"))
Y=float(input("Enter 2nd/Y number:"))
Z=float(input("Enter 3rd/Z number:"))
if(X>Y and X>Z):
    print("X is greater value")
elif(Y>X and Y>Z):
    print("Y is greater value")
elif(Z>X and Z>Y):
    print("Z is greater value")'''

#_4 WAP if a number is multiple of 7 or not?
Num=float(input("Enter Number"))
if(Num%7==0):
    print("Multiple of 7")
else:
    print("Not multiple of 7")