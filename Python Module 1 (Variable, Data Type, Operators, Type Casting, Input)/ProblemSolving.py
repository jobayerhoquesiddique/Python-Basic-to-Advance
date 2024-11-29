"""Problem 1: Basic Variables and Data Types
Write a Python program that does the following:
1.Assigns your name to a variable.
2.Assigns your age to another variable.
3.Prints a message saying "Hello, my name is [name] and I am [age] years old."""
name = "Jobayer"
age=23
print("Hello, my name is", name,"and I am",age,'years old')

"""Problem 2: Write a Python program that:
Takes two numbers as input from the user.
Computes the sum, difference, product, and quotient of these numbers.
Prints the results"""
X=float(input("Enter 1st number"))
Y=float(input("Enter 2nd number"))
sum=X+Y
print(sum)
diff=X-Y
print(diff)
pro=X*Y
print(pro)
que=X/Y
print(que)

"""Problem 3: Write a Python program that:
Takes a string input from the user.
Converts this string to an integer and a float.
Prints the results of these conversions."""

x=int(input("Enter an int value"))
y=float(input("Enter an float value"))
sum=x+y
print(sum) 
#///from chatgpt
user_input=input("Enter Value")
float=float(user_input)
int=int(user_input)
print("Float:",float)
print("integer:",int)

"""Problem 4:Write a Python program that:
Takes the radius of a circle as input from the user.
Computes the area of the circle using the formula 𝜋×radius^2.
Prints the area. Use 'math.pi' for the value of π."""

Radius=float(input("Enter radius value"))
mathpi=3.1416                                                                #'math.pi'
Area_of_circle=mathpi*Radius**2
print(Area_of_circle)

"""Problem 5:Write a Python program that:
Takes a temperature in Celsius as input from the user.
Converts this temperature to Fahrenheit using the formula of Fahrenheit=(Celsius× 9/5 )+32.
Prints the temperature in Fahrenheit."""
Celsious=float(input("Enter tempurature"))
Fahrenheit=(Celsious*9/5)+32
print(Fahrenheit)

"""Problem 6: Shopping Cart Total
Write a Python program that:
Takes the prices of three items as input from the user.
Computes the total cost.
Prints the total cost."""
Bag=int(input("Price of Bag:"))
Shoe=int(input("Price of Shoe:"))
Chain=int(input("Price of Chain:"))
Total_Cost=Bag+Shoe+Chain
print("Your total cost is:",Total_Cost,"taka")

"""Problem 7: BMI Calculator
Write a Python program that:
Takes the user's weight in kilograms and height in meters as input.
Computes the Body Mass Index (BMI) using the formula BMI=weight/height^2
Prints the BMI."""
Weight=int(input("Enter your weigth in kg:"))
Height=float(input("Enter your height in meter:"))
BMI= Weight/Height**2
print(BMI)

"""Problem 8: Simple Interest
Write a Python program that:
Takes the principal amount, rate of interest, and time (in years) as input from the user.
Computes the simple interest using the formula Simple Interest=(Principal×Rate×Time)/100.
Prints the simple interest."""
Ammount=int(input("Enter ammount taka:"))
Interest_Rate=float(input("Enter rate of interest in %:"))  #%
Time= int(input("Enter total year:"))
Simple_Interest=(Ammount+Interest_Rate+Time)/100
print(Simple_Interest)

"""Problem 9: Comparing Numbers
Write a Python program that:
Takes two numbers as input from the user.
Compares the numbers and prints which one is larger, or if they are equal."""
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
print(not(a>=b))
print(not(a<=b))
#print(a>=b and a<=b)
#from chatgpt although
k=int(input("Enter 1st number:"))
l=int(input("Enter2nd number"))
if(k>=l):
    print("K is lagrger number")
else:
    print("l is samll or they are not equal")


"""Problem 10: Even or Odd
Write a Python program that:
Takes an integer as input from the user.
Determines if the number is even or odd.
Prints the result."""
Num=int(input("Enter Vlaue:"))
Even= Num%2 ==0
Odd= Num%2 !=0
Result=Even or Odd
print(Result)

num=int(input("Enter any number:"))
if( num%2 == 0 ):
    print("Even")
else:
    print("Odd")

"""Problem 11: String Operations
Write a Python program that:
Takes a string input from the user.
Prints the length of the string.
Converts the string to uppercase and prints it.
Converts the string to lowercase and prints it."""
Value=input("Enter the text")
print(len(Value))
X=Value.upper()               #StringMethod
y=Value.lower()
print(X) 
print(y)
print(type(X))

"""Problem 12: Real-World Scenario - Restaurant Bill
Write a Python program that:
Takes the cost of a meal, the tax rate, and the tip percentage as input from the user.
Computes the total cost of the meal.
Prints the total cost. Use the following formulas:
Tax amount = cost of meal * (tax rate / 100)
Tip amount = cost of meal * (tip percentage / 100)
Total cost = cost of meal + tax amount + tip amount"""
Welcome=input("This is your Bill memo sir,")
Cost_of_the_meal=int(input("Your meal costed:"))
Tax_rate=int(input("Charged with tax:"))
Tipp=int(input("You tipped :%,of"))

Tax_Ammount=Cost_of_the_meal*(Tax_rate/100)
Tip_Ammount=Cost_of_the_meal*(Tipp/100)
Total_Cost=Cost_of_the_meal+Tax_Ammount+Tip_Ammount
print("Here is the total cost:",Total_Cost)