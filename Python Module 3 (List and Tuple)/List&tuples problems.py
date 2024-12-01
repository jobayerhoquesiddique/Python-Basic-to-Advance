"""Problem 1: Grocery List
You are planning to go grocery shopping. Create a list called grocery_list that contains the following items:
'apples', 'bananas', 'milk', 'bread', and 'eggs'.
1.Print the number of items in your grocery list.
2.Add 'chicken' and 'rice' to your grocery list.
3.Remove 'bread' from the list.
4.Check if 'milk' is in your list, and print a message confirming whether it is or isn't.
Print the final list."""
'''List=['apples', 'bananas', 'milk', 'bread','eggs']
print("Total Iteam:", len(List))
List.insert(0,'chicken')
List.insert(5,'rice')
print("List after adding chicken&rice:",List)
List.remove('bread')
print("List after removing bread:",List)
if(List.count('milk')):
    print("It has")
else:
    print("Isn't")
print("Final Grocery list:",List)
'''
"""Problem 2: Travel Itinerary
You are planning a trip and want to create a travel itinerary. Create a tuple called itinerary
that contains the following destinations in order: 'New York', 'Paris', 'Tokyo', and 'Sydney'.
1.Print the first and last destinations in your itinerary.
2.Check if 'London' is in your itinerary and print an appropriate message.
3.Tuples are immutable, so create a new tuple called updated_itinerary by adding 
'London' to the end of the original itinerary.
Print the new itinerary."""

'''Destination=('New York', 'Paris', 'Tokyo','Sydney')

if(Destination.count('London')):
    print("Yes it has london")
else:
    print("No it dosen't have london")
Updated_Destination=list(Destination)
print(Updated_Destination)
Updated_Destination.append('london')
print(Updated_Destination)
print("First Destination:",Updated_Destination[0])
print("First Destination:",Updated_Destination[-1])
print(Updated_Destination)'''

"""Problem 3: Student Grades
You are a teacher and need to manage student grades. Create a list called grades that 
contains the following grades: 85, 92, 78, 90, and 88.
Calculate and print the average grade.
Add a new grade 95 to the list.
Find and print the highest and lowest grades in the list.
Sort the grades in descending order and print the sorted list."""

'''Grade=[85,92,78,90,88]
a=Grade[0]
b=Grade[1]
b=Grade[2]
c=Grade[3]
d=Grade[4]
len=len(Grade)
Sum=(a+b+c+d)
Avg=Sum/len
print("Average grade:",Avg)
Grade.append(95)
print(Grade)
print("Lowest Mark:",max(Grade))
print("First Mark:",min(Grade))
Grade.sort(reverse=True)
print(Grade)'''

"""Problem 4: Favorite Movies
You want to keep track of your favorite movies. Create a list called favorite_movies that
contains at least five movie names.
Print the list of favorite movies.
Add a new movie to the list.
Remove a movie from the list.
Print the movie that is currently at the third position in the list.
Check if a specific movie (e.g., 'Inception') is in your list and print a message."""

'''a=(input("Enter your first movie:"))
b=(input("Enter your second movie:"))
c=(input("Enter your third movie:"))
d=(input("Enter your fourth movie:"))
e=(input("Enter your fifth movie:"))
Favorite_Movie=[a,b,c,d,e]
print(Favorite_Movie)
Favorite_Movie.append(input("Enter new movie:"))
print(Favorite_Movie)
print("After removing:",Favorite_Movie.pop())
print("Third movie:",Favorite_Movie[0])
if(Favorite_Movie.count("Kigsman")):
    print("Yes it has")
else:
    print("No")'''


"""Problem 5: Weekly Temperature
You want to record the daily temperatures for a week. Create a tuple called weekly_temps that 
contains the temperatures for seven days: 70, 72, 68, 65, 74, 75, 73.
Calculate and print the average temperature for the week.
Find and print the highest and lowest temperatures of the week.
Convert the tuple to a list and change the temperature of the fourth day to 67. Print the updated list.
Print the temperatures that are above 70."""

'''Weeklytemperature=[70, 72, 68, 65, 74, 75, 73]
len=len(Weeklytemperature)
a=Weeklytemperature[0]
b=Weeklytemperature[1]
c=Weeklytemperature[2]
d=Weeklytemperature[3]
e=Weeklytemperature[4]
f=Weeklytemperature[5]
g=Weeklytemperature[6]
Avg=(a+b+c+d+e+f)/len
print(Avg)
print("The lowest temp:",min(Weeklytemperature))
print("The Highest temp:",max(Weeklytemperature))
X=list(Weeklytemperature)
X.insert(3,67)
print("After filling4th:",X)
if(a>=70):
    print("1stnumber",a)
if(b>=70):
    print("2nd number:",b)
if(c>=70):
    print("3rd number",c)
if(d>=70):
    print("4th number:",d)
if(e>=70):
    print("5th number:",e)
if(f>=70):
    print("6th number:",f)
if(g>=70):
    print("7th number:",g)'''
