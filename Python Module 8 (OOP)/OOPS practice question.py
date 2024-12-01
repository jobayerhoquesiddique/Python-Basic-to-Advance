"""Practice Question"""
#Define a circle class to create a circle with radius r using the contstructor
#Define an Area () method of the class which calculates the area of circle.
#Define a Perimeter() method of the class which allow you to calculate the perimeter of the circle 

class Circle:
    def __init__(self,radius):
        self.radius= radius

    def Area(self):
        return 3.1416 * self.radius ** 2
    def perimeter(self):
        return 2*3.1416*self.radius
    

Circle_Radius = Circle(7)
print(Circle_Radius.Area())
print(Circle_Radius.perimeter())

#Define a Employee class with attributes role, department & salary.This class also have a
#  showDetails() method
#create an engineer class thath inherits properties from Employee & has additional attributes
#name & age 
class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print("Role = ",self.role)
        print("Dept =",self.department)
        print("Salary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75000")

E1 = Engineer("Md Joba",40)
E1.showDetails()
E2=Employee("CEO","R&P","54151")
E2.showDetails()

#Create a class called order which stores item & its price.
#use Dunder function __gt__ to convey that
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price > ord2.price

Ord1= Order("Chips",20)
ord2=Order("Banana",45)
print(Ord1>ord2)
print(ord2>Ord1)
        