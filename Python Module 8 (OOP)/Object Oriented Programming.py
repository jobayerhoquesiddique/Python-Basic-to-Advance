"""Object Oriented Programming"""
#To map the real world scenario we started using objects in code
#This is called object oriented programming 
"""Object and Class"""
#Class is a blueprint for creating an object
#Creating a class 
class Student():
    #class attribute
    name=["Jobayer","Jobayda","Chamely"]
    '''Age={ "Jobayer":23,
          "Jobayda":8,
          "Mozammel":56
            }'''
    def __init__(self,Phone,Blood):
        #object attribute
        self.Phone= Phone
        self.Blood = Blood    #Object attribute < Class attribute
    def bloodtype(self):
        print("Your blood group is :",self.Blood)
#creating an object
s=Student("01400144611","O+")
print(s.Phone,s.Blood)
print(s.name)
s.bloodtype()

#Practice Question
#Create student class that takes name and marks of 3 subject as arguments in constructor.
#Then create a method to print their average
class Marks():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

        self.len = len(marks)
        self.sum = sum(marks)
        self.avg = self.sum/self.len

M=Marks("jobayer",[74,56,96])
print(M.name,M.avg)
"""From YT"""
class Student:
    def __init__(self,name,marks,len):
        self.name = name
        self.marks = marks
        self.len = len(marks)
    #Static Method 
    @staticmethod   
    def hello():
        print("Hallo")    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"your average value is:",sum/self.len)
MOS=Student("Jobayer:",[45,96.178,200],len)
MOS.get_avg()

MOS.name="Bruce Wyne"
MOS.get_avg()
MOS.hello()

"""Abstraction"""
#Hiding the implementation details of a class and only showing the
#essential features to the user
"""Let's Practice"""
#Create account class with two attributes - balance & account no
#Create methods for debit & credit & printing the balance
class Account:
    def __init__(self,Balance,Account_no):
        self.Balance = Balance
        self.Acccount_no = Account_no
    #debit_method
    def debit(self,ammount):
        self.Balance -= ammount
        print("BDT",ammount,"was debited from acc")
        print("Total Balance is :", self.get_bal())
    def credit(self,ammount):
        self.Balance += ammount
        print("BDT",ammount,"was credited from acc")
        print("Total Balance is :", self.get_bal())
    
    def get_bal(self):
        return self.Balance

acc = Account(10000,1234505)
acc.debit(100)
acc.credit(500)
acc.credit(400)
acc.debit(1000)
acc.get_bal()

"""Del keyword"""

class Student():
    def __init__(self,name):
        self.name = name

s=Student("Jobayer")
print(s.name)
"""del s.name         #del keyword
print(s.name)"""

"""Private like attributes & methods"""
#Conceptual implementation in python 
#Private attributes & methods are ment to be used only within the class.
#and are not accessible from outside the class

class Bank:
    def __init__(self,acc_name,acc_pass):
        self.__acc_name = acc_name#(__This is private key)
        self.acc_pass = acc_pass
    def getaccname(self):
        print(self.__acc_name)
    
Acc=Bank("Jobayda","05436")
#print(Acc.__acc_name)  
print(Acc.acc_pass)
print(Acc.getaccname())

"""Inheritance"""
#Single Inheritance 
class Zilla:
    @staticmethod
    def upazilla():
        print("Nawabganj")

    @staticmethod
    def upazilla1():
        print("Savar")

class Divvision(Zilla):
    def area(self,name):
        self.name = name

#Multi-Level Inheritance 
class seat(Divvision):
    def __init__(self,seat):
        self.seat = seat

BD = seat("1")
BD.upazilla()
"""Area_of_Choice = Divvision
print(Area_of_Choice.upazilla())"""

#Multiple Interitace
class messi():
    def __init__(self,ctrg):
        self.ctrg = ctrg
    type="the debate is over"

class ronaldo():
    type1="Mr.Ucl"

class neymar(messi,ronaldo):
   
   type2="Bad person"
   

Player = neymar("National")
print(Player.ctrg)
print(Player.type)
print(Player.type1)
print(Player.type2)

"""Class Method"""
#Static method is bound to the class & receives the class as an implicit first 
#argument _Note:Static method can't access or modify class state & generally for utility
#Class Method
class Uni:
    name="DIU"
    name2="NSU"
    name3="BracU"
    @classmethod
    def UNI(self,name):
        self.name=name
    
Rank=Uni
Rank.UNI("AIUB")
print(Rank.name)

#Property mehtod 
#We use the property decorator on any method in the class to use 
#the method as property
class Marks:
    def __init__(self,phy ,cam,math):
        self.phy=phy
        self.cam=cam
        self.math= math
        #self.avg=str((self.math+self.phy+self.cam)/3)+"%"

    @property
    def percent(self):
        return str((self.math+self.phy+self.cam)/3)+"%"


Stu1=Marks(98,97,99)
print(Stu1.percent)

Stu1.math=100
Stu1.cam=69
print(Stu1.percent)
"""Polymorphism : Operator Overloading"""
#When the same operator is allowed to have different meaning according to the context
#  Dunder(__)     operator
#1.__add__      a+b
#2.__sub__      a-b
#3.__mul___     a*b
#4.__truediv____ a/b
#5.__mod____     a%b 

"""Lets create Operator Overloading using Dunder"""
class Complex:
    def __init__(self,real,img):
        self.real= real
        self.img=img

    def showNum(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,addition):
        NewReal= self.real + addition.real
        NewImg = self.img + addition.img
        return Complex(NewReal, NewImg)
    
    def __sub__(self,subm):
        NewReal= self.real - subm.real
        NewImg = self.img - subm.img
        return Complex(NewReal, NewImg)
    
    def __mul__(self,mult):
        NewReal= self.real * mult.real
        NewImg = self.img * mult.img
        return Complex(NewReal, NewImg)
    
    def __truediv__(self,div):
        NewReal= self.real / div.real
        NewImg = self.img / div.img
        return Complex(NewReal, NewImg)
    
    def __mod__(self,mod):
        NewReal= self.real % mod.real
        NewImg = self.img % mod.img
        return Complex(NewReal, NewImg)

Num=Complex(7,3)
Num.showNum()
Num1=Complex(3,6)
Num1.showNum()

num2 = Num+Num1
num2.showNum()

num3 = Num-Num1
num3.showNum()

num3 = Num*Num1
num3.showNum()

num4 = Num/Num1
num4.showNum()

num4 = Num%Num1
num4.showNum()