#This is our first lesson. We are gonna learn(VARIABLE,Data Type,Types of operator,Type Casting,Input)
"""Our Firt Program"""
print("Jobayer")

"""Variable"""
#It is a name given to memory location in a program.
name="Joayeda"
age=9
Dob="17/04/2016"
print(name)
print(age)
print(Dob)

"""Data Types"""
#Multiple data types includes Integer(int),Float(float),String(sum of sentences),Boolean(True/False),None
Age=2
Saving=3.5
sum_Word="With Islam series"
is_adult=True
Marrige=None #
print(type(Age))
print(type(Saving))
print(type(sum_Word))
print(type(is_adult))
print(type(Marrige))

"""Comments"""
# ctrl + / to select bunch of line and comment
#This is a comment 
# ctrl + / to select bunch of line and comment
"""
This is a 
multi line 
comment

"""

"""Types of Operator"""
#Operator is a symbol that perform certain operation between operands.These are
#_"1"Arithmetic Operators(+,-,*,/,%,**)
#_"2"Relational/Comparison(==,!=,<,>,>=,<=)
#_"3"Assignment Operator(+=,-=,*=,/=,%=,**=)
#_"4"Logical Operators(and,or,not)

#1_Logical Operator(and,or,not)
a=1
b=4
print(a+b)
print(a-b) 
print(a*b)
print(a/b)
print(a%b)
print(b**a)
#2_Relational/Comparison(==,!=,<,>,>=,<=)
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#3_Assignment Operator(=,+=,-=,*=,/=,%=,**=)
num=20
num=num+5
print(num)

num1=20
num1+=5
print(num1)

num2=20
num2-=5
print(num2)

num3=20
num3*=5
print(num3)

num4=20
num4/=5
print(num4)

num5=20
num5%=5
print(num5)

num6=20
num6**=5
print(num6)

#4_Logical Operators(and,or,not)
x=12
y=23
print(x>y)      
print(not(x<y))    #Not create the oposite answer of expression
print(not(x>y))

Jobayer_is_adult=True
Jobayda_is_adult=False
Jobayda_not_adult=True
print(Jobayer_is_adult and Jobayda_not_adult) #TTandFF
print(Jobayer_is_adult or Jobayda_is_adult)   #onlyTrue

"""Type Conversion"""

"""Type Casting"""
#Convert or cast values into different datatypes
g=int(10)
d=float(10.0)
print(g+d)
print(type(g))
print(type(d))

"""Input in Python"""
#Input statement is used to accept values(from terminal)from the user
#input is always a string tyoe
V=input("Fill this form")
Name=input("Enter your name:")
Age=input("Enter your age")
Salary=input("Enter your salary")
print("Welcome:",V)
print("Your name is:",Name)
print("Your age is:",Age)
print("Your salary:",Salary)

""""PRACTICE EXCERCISE"""
#_1Write a program to enter 2 number & print their sum
p=float(input("Enter 1st number"))
q=float(input("Enter 2nd number"))
sum=p+q
print(sum)

#_2Write a program to input side of a square and print its area 
r=int(input("Side of square 1:"))
w=int(input("Side of square 2:"))
Area=(r*w)
print(Area)

#_3Write a program to input two floating point number & print their average
Num1=float(input("Enter your first number"))
Num2=float(input("Enter your 2nd number"))
Num3=float(input("Enter your 3rd number"))
W=Num1+Num2+Num3
Average=W/3
print(Average)

#_4Write a program to input two int number, a and b.Print True if a is greater than or equal to b.
# If not print false  
K=int(input("Enter number"))
L=int(input("Enter 2nd number"))
print(K>L or K<L)