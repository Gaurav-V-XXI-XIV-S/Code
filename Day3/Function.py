# def arithmatic():
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
 
# result=arithmatic()
# print("Arithmatic =",result)

# # Question:- is it possible to write multiple value 
# # yes it is possible to write multiple value
#.......................................................................................#

#_______________________________Positional Argument_____________________________________#
# def arithmatic(a,b):
#     sum = a + b
#     sub = a - b
#     div = a / b
#     mul = a * b
#     return sum, sub, div, mul

# result = arithmatic(5,5)
# print("Arithmatic =",result)
#.......................................................................................#

#_________________________________Key Argument__________________________________________#
# def credential(username, password):
#     if username == password:
#         print("login Successfully ")
#     else:
#         print("Invalid Credentials ")

# credential(username = "admin", password = "admin")
#.......................................................................................#

#_______________________________Default Argument________________________________________#
# def cityname(city="Pune"):
#     print(city)

# cityname("nagpur")
# cityname("Mumbai")
# cityname()
#.......................................................................................#  


#_____________________________Variable Length Argument__________________________________#
# def cityname(*name):
#     print(name)

# ciryname("Nagpur", "Delhi", "Mumbai", "Pune")
#.......................................................................................#

#______________________Modularity Approach In Function__________________________________#
import sys
def add():
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    print(a+b)

def sub():
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    print(a-b)

def div():
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    print(a/b)

def mul():
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    print(a*b)

while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        add() 
    elif choice == 2:
        sub()
    elif choice == 3:
        div()
    elif choice == 4:
        mul()
    elif choice == 5:
        sys.exit()
    

