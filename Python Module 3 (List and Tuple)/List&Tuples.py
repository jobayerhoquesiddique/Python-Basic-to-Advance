#Lecture 3 (List,Tuples)
"""List"""
#A built in data type that stores a set of values .Can be (int,float,string)
Info=["Jobayer",23,"Dhaka",'000000']
Info[1]="ILOK"
print(Info[3])
"""List Slicing"""
Info[1:4]
print(Info)
"""List Methods"""
Student=["Jobayer","Nawabganj",23,2.09,"Apple"]
Student.append("Wannabecs")
Student.sort()
Student.sort(reverse=True)
Student.reverse()
Student.insert(2,"No one")
print(Student)

"""Tuple"""
#let us create immutable value 
tup=("Jobayer",4538,'DHAKA1320',".",",","")
print(tup[0])
s=tup.count(4538)
print(s)
tup + ("virtue","knight")
print(tup)
"""PRACTICE QUESTION"""
#1_WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
x=input("Enter first movie :")
y=input("Enter first movie :")
z=input("Enter first movie :")
list=list()
list.insert(0,x)
list.insert(1,z)
list.insert(2,y)
list.pop()    #it removes the last item 
print(list)

#_2WAP to cheack if a list contain a palindrom or not(Use copy method)
"""[1,2,3,2,1] , [1,"abc","abc",1]"""
Pal=[1,2,3,2,1]
Pal1=Pal.copy()

Pal1.sort(reverse=True)

if(Pal==Pal1):
    print("Pallindrom")
else:
    print("not")

#WAP to count the number of students with the “A” grade in the following tuple.
Grades=["C","D","A","B","B","B","A"]
A=Grades.count("A")
print(A)
#Store the above values in a list &store them from A-D
Grades.sort()
print(Grades)