"""Dictionary"""
#Dictionaries are used to store data values in{key:Value} pairs.
#They are mutable,unordered and dosen't allow duplicate keys 
'''info={
    "name":"Jobayer",
    "age":23,
    "cgpa":"1.92"
}
print(info)
print(info["name"])
print(info["age"])
print(info["cgpa"])
'''
"""Nested dictionaries"""
'''student={
    "name":"Jobayer",
    "age":'23',
    "CGPA":{
        "spring24":0.96,
        "Fall":2.78,
        "spring23":0.5
    }
}
print(student["CGPA"])
print(student["CGPA"]["spring23"])'''

"""Dictionary method """
'''village={
    "name":"Gulshan",
    "age":1809,
    "divission":"Dhaka"
}

print(village.keys())
print(village.values())
print(village.get("name"))
print(village.items())
village.update({"Isgood":"No",})
print(village)'''

"""set"""
#Set is the collection of unordered iteam 
#set is immutable and must be unique 
'''num={1,2,3,4,5}
hi={1,2,2,4,5} #2 wont be print
print(num)
print(hi)

"""set method"""
info={"Hazrat Muhammad (Sa)",1,"World",'Massenger'}
info1={1,1,2,3,4,5,"Abu Bakr(Ra)","World","Khalifa"}
info2={1,2,2,4,5,"Umaar(Ra)","World","Khalifa"}
print(info.union(info1))
print(info1.union(info2))
print(info1.intersection(info2))'''

"""PROBLEM EXCERCISE"""
#Problem1_:Store the word meaning in a python dictionary
#"table"="a piece of furniture","list of facts & figure"
#"cat"="a small animal"
'''Word={
    "table":{"a piece of furniture ","list of facts & fugure"},
    "cat":"a small animal"
}
print(Word)'''

#Problem2:You are given a list of subject for students.Assume 1 classroom is given for one subject.
# How many classroom are needed by all student.
#"python","java","C++"","python","javascript","java","python","java","C++","C"
'''Subject={"python","java","C++","python","javascript","java","python","java","C++","C"}
print("Total Subject:",Subject)
print("Total Classroom:",len(Subject))'''

#Problem3_:WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#an empty dictionary & add one by one. Use subject name as key & marks as value.
'''Mark={}
Mark.update({"Phy":"109"})
Mark.update({"Chem":"9"})
Mark.update({"CS":"19"})
print(Mark)'''

#Problem4_;Figure out a way to store 9 & 9.0 as separate values in the set.
#(You can take help of built-in data types)

'''o=list(set())
a=9
b=10
o.append(a)
o.append(b)
print(o)'''

#Problem 1: Email Directory
'''You are creating a contact directory for your company. Each employee has a name and an email address.
1.Create a dictionary where the keys are employee names, and the values are their email addresses.
2.Write a function add_employee(directory, name, email) to add a new employee to the directory.
3.Write a function find_email(directory, name) to find the email address of an employee by their name.
  If the name is not found, return a message indicating that.
4.Write a function update_email(directory, name, new_email) to update the email address of an existing employee.'''
'''Contact={
    "Jobayer":"jubucse@gmail.com",
    "Mozammel":"wmemorialhs@gmail.com",
    "Chamely":"chamely@gmail.com",
    "Jobayda":"jobayda@gmail.com"
}
print(Contact)
add_employee=({"umar":"umar321@gmail.com"})
Contact.update(add_employee)
print("New employee:",Contact)
Find=Contact.get(input("enter value"))
if(Find):
    print("Your directory:",Find)
else:
    print("Not found")
Contact.update({"Jobayer":"jhs4538@yahoo.com"})
print((Contact))
'''
"""Problem 2: Word Frequency Counter
You are given a paragraph of text. You need to count the frequency of each word in the paragraph.
Tasks:
Write a function word_frequency(text) that takes a string text and returns
a dictionary with words as keys and their frequencies as values.
Ensure that the function ignores punctuation and is case-insensitive."""
'''Peragraph={"There is a big possibility that something is around you can shift your everything"}
print(Peragraph.)
'''
'''Problem 3: Student Grades
You are managing a record of student grades in a class. Each student has a name and a list of their grades.
Tasks:
Create a dictionary where the keys are student names, and the values are lists of their grades.
Write a function add_grade(record, name, grade) to add a grade to a student's record.
Write a function calculate_average(record, name) to calculate the average grade for a student.
 If the student does not exist, return a message indicating that.'''

'''Student_grade={
    "Jobayer":{"Phy":45,"Chem":49,"Bio":93},
    "Jobayda":{"Math":45,"Bangla":78,"Eng":23}
}
print(Student_grade)
x=str(Student_grade.update("Jobayda":))
x.join("Math1,:00")
print(x)'''

"""Problem 4: Inventory Management
You are managing the inventory for a small store. Each item has a name and a quantity.
Tasks:
1.Create a dictionary where the keys are item names, and the values are their quantities.
2.Write a function add_item(inventory, item, quantity) to add a new item to the inventory 
 or update the quantity of an existing item.
3.Write a function check_stock(inventory, item) to check the quantity of a specific item. 
 If the item is not found, return a message indicating that.
4.Write a function remove_item(inventory, item, quantity) to remove a certain quantity of an item from the inventory.
 If the quantity to be removed is more than the available quantity, remove the item completely."""

Jobaconvention={
    "Biscuite":1,
    "Banana":2,
    "Pencil":4,
    "Hat":6,
    "Coffe":8
}
print("The iteams are:",Jobaconvention)
Jobaconvention.update({"Nestly":56})
print("New added iteam:",Jobaconvention)
Jobaconvention.pop(input("remove an item"))
print("After removing an item:",Jobaconvention)
