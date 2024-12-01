'''"""PRACTICE lecture 7"""
#Create a new file "practice.txt" using python.Add the
#  following line in the data
#Hi everyone
#We are learning File I/O
#using Java
#I like programming in Java
with open("pracice.txt","w") as f:
    f.write("Hi everyone\nWe are learning FileI/O")
    f.write("\nusing Java\nI like programming in Java")
#WAF to replace Java with Python :
with open("pracice.txt","r") as f:
    data=f.read()
    
newdata=data.replace("Java","python")
print(newdata)
with open("pracice.txt","w") as f:
    f.write(newdata)
#WAF to find a word :
def cheak_for():
    word=input("Enter word:")
    with open("pracice.txt","r") as f:
        Data=f.read()
    if(Data.find(word)!=-1):
        print("Found")
    else:
        print("Not found")

cheak_for()

#WAF to find in which line of the file the word "learning"
#occur first .Print -1 if not found
def find_word():
    word="python"
    data=True
    line_no=1
    with open("pracice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return-1
find_word()

with open("pracice.txt","r") as f:
    deta=f.read()
    repl=deta.replace("Java","c++")
    print(repl)
    with open("pacice.txt","w") as f:
        f.write(repl)'''
#From a file containing number seperated bt comma .Print the count
#even numbers.
count=0
with open("pracice.txt","r") as f:
    deta=f.read()
    
    num=deta.split(",")
    for val in num:
        if(int(num)%2 ==0):
            count += 1

print(count)
