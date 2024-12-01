"""Function"""
#Function is a block of statement that perform a specific task
#1_WAF to print length of a list

n=[1,2,4,5,3,6,7,8,0]
def len_list(list):
    print(len(list))
len_list(n)
#write a function print the element of a list in a  single line
Num =(1,3,4,5,7,8)
def el_list(list):
    print(list)

print(Num)

#WAF to find the factorial of n (n in perameter)
def cal_fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
        print(fact)

cal_fact(7)

#Wap to convert USD to BDT
def convert(USD):
        
        BDT=USD*114
        print(BDT)

convert(100)
#WAF if number is ODD or EVEN
def Num_type(Num):
        
        if(Num%2==0):
            print("EVEN")
        else:
            print("ODD")

Num_type(4)

#Write a function to print length of a list(List in perameter )
def len_list(input_list):
     print(len(input_list))

len_list((1,2,3,4,5,6,8,9))
len_list(("Jobayer","Jobayda","Chamely","Mozammel"))

#WAF to print the element of the list in a sinle line (List in the perameter)
def el_in_list(enter_list):
     for element in enter_list:
         print(element,"",end="")

el_in_list(["Batman","Ironman","MansaMusa","Elon Musk"])

#WAF to find the factorial of n.(n in the perameter)
def facto(a):
    fact=1
    for i in range(1, a+1):
        fact*=i
    print(fact)

facto(6)

#4WAF to convert USD to BDT
def convert(USD):
    BDT = USD*114
    print(USD,"USD=",BDT,"TAKA")

convert(100)
    
#5 WAF to print if a input number is "ODD"or"EVEN
def Num_type(Num):
    if(Num%2==0):
        print("EVEN")
    else:
        print("ODD")

Num_type(56)

"""Recursion"""   
#When a function calls itself repeatedly
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

print(show(5))

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)
    
print(fact(5))
