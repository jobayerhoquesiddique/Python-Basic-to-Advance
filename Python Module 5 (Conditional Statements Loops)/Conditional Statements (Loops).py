"""Loops"""
#While Loops
"Lets Practice"
#Print Numbers from 1-100
'''u = 1
while u<=100:
    print(u)
    u+=1'''

#2_Print Numbers from 100-1
'''i = 100
while i>=1:
    print(i)
    i-=1'''

#3_Print the multiplication table of number n
'''i=1
n=int(input("Enter number:"))
while i<=10:  #stop condition
    print(n*i)
    i+=1'''
#4_Print the element of the following list using while loops 
#[1,4,9,16,25,36,49,64,81,100]
'''num=[1,4,9,16,25,36,49,64,81,100]
indx=0
while indx<len(num):
   
    print(num[indx])
    indx+=1'''
#5_Search for a number x in this tuple using loop
#[1,4,,9,16,25,36,49,64,81,100]
'''num=[1,4,9,16,25,36,49,64,81,100]
x=int(input("Enter your num:"))
indx=0 #initialization
while indx<len(num):
    
    if(num[indx]==x):
        print("found at index",indx)
    else:
        print("finding")
    indx+=1 '''
        
"""Breaks & Continue"""
#Break
'''num=[1,4,9,16,25,36,49,64,81,100]
x=int(input("Enter your num:"))
indx=0 #initialization
while indx<len(num):
    
    if(num[indx]==x):
        print("found at index",indx)
        break
    else:
        print("finding")
    indx+=1'''
    
#Continue
'''num=[1,4,9,16,25,36,49,64,81,100]
num=0
while num <= 10:
    if(num%2 == 0):
        num+=1
        break
    print(num)
    num+=1'''
 
#for loops 
#for loops are used for sequentioal traversal
'''tup=(1,5,7,9,56,66,77,58,74,65)
for num in tup:
    if(num==66):
        print("Found")
        break
    else:
        print("Finding")
'''
"""Print the Element of the following list using for loop"""
#[1,4,9,16,25,36,49,64,81,100]
'''num=[1,4,9,16,25,36,49,64,81,100]
for value in num:
    print(value)'''

#Search for the number x in the following tuple using loop
#[1,4,9,16,25,36,49,64,81,100]
'''num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter number:"))
indx=0
for char in num:
    if(char == x):
        print("The number found at",indx)
        break
    indx+=1'''
        
'''Range'''
#Range functions returns a set of numbers 
#Range(start,stop,step)
'''seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
for i in seq:
    print(i)'''

'''for el in range(10):
    print(el)
for el in range(2, 10):
    print(el)
for el in range(1, 10 ,3):
    print(el)'''
    
"""Practice using for and  range"""
#Print numbers from 1 to 100
'''for i in range(1,101):
    print(i)'''

#Print numbers from 100 to 1
'''for i in range(100,0,-1):
    print(i)'''
       
        
#Print the multiplication number of n
'''num = int(input("Enter number"))
for el in range(1,11):
    print(num*el)'''

"""Pass Statement"""
#Pass statement is a null statment that does nothing .It is used for future code 
'''for el in range(10):
    pass
print("InshAllah")'''

 #WAP to find the sum of first n  number using for loop
'''num = 7
sum=0
for i in range(num+1):
    sum+=i
print("Total sum of number:",sum)'''

#WAP to find the sum of first n  number using while loop

'''num=7
i=1
sum=0
while i<=num:
    sum+=i
    i+=1
    print("Sum of 9:",sum)'''
   
#WAP to find the factorials of first n numbers 
'''num=5
fact=1

for i in range(1,num+1):
    fact*=i
  
    print("Fact:",fact)'''
'''num=9
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
    print(fact)'''