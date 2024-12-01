class Zilla:
    def __init__(self,type):
        self.type = type
    Seat_no="1"
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
        #supertype
        super().__init__(type)
        self.seat = seat
     

"""BD = seat("average",1)
print(BD.type)
BD.upazilla()
BD.area("Big")"""

Area_of_Choice = Divvision
Area_of_Choice.upazilla()
print(Area_of_Choice.upazilla1())


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
#Class Method
"""class Uni:
    name="DIU"
    name2="NSU"
    name3="BracU"
    @classmethod
    def UNI(self,name):
        self.name=name
    
Rank=Uni
Rank.UNI("AIUB")
print(Rank.name)"""

#Property mehtod 
#We use the property decorator on any method in the class to use 
#the method as property
"""class Marks:
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
print(Stu1.percent)"""

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