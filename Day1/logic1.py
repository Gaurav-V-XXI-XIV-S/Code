# # simple if
# print(2+2)
# print("2"+"2")
# a = input("Enter a number: ")
# b = input("Enter another number: ")
# print(a+b)

# #int() is used to convert string to integer 3.14=int=3
# print(int(3.14))
# #print(int(10.5j))
# print(int(True))
# print(int(False))
# #print(int("4.2210"))
# print(int("4"))

# #Float() is used to convert string to float 3=int=3.0
# print(float(3))
# #print(float(10.5j))
# print(float(True))
# print(float(False))
# #print(float("4.2210"))
# print(float("4"))

# # complex() is used to convert string to complex 3=int=3+0j
# print(complex(3))
# print(complex(3.14))    
# print(complex(True))
# print(complex(False))   
# print(complex("5"))
# print(complex("5.14"))  
# #print(complex("name"))
# print(complex(10.5 , -3))
# print(complex(True , False))

# #bool() is used to convert string to boolean 3=int=True 0=int=False
# print(bool(3))
# print(bool(0))      
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(True))
# print(bool(False))
# #print(bool(""))
# #print(bool("Gaurav"))

# #   simple if 
# a = int(input("Enter first number: "))
# if a > 0:
#     print("Positive Number")    
# if a < 0:
#     print("Negative Number")
# if a == 0:
#     print("Zero")    

#simple if in finding working day or weekend day

# day = input("Enter a day: ")
 

# print("Lowercase:", day.lower())
# print("Uppercase:", day.upper())

# if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
#     print("Working Day")

# elif day == "saturday" or day == "sunday":
#     print("Weekend")

# else:
#     print("Invalid Day")


# # simple calculator using if-else statement
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# choice = int(input("Enter choice: "))
# if choice == 1:
#     print("Result =", a + b)
# elif choice == 2:
#     print("Result =", a - b)
# elif choice == 3:
#     print("Result =", a * b)
# elif choice == 4:
#     print("Result =", a / b)
# else:
#     print("Invalid Choice")
    

# #multiple if-else statement
# per=90
# if per >=65:
#     print("First Division")
# elif per <=65 and per >=50:
#     print("Second Division")
# else:
#     print("Fail")

# A=65
# a=97
# 0=48

# chr = ord(input("Enter a character: "))
# if chr >= 65 and chr <= 90:
#     print("Uppercase Letter")\
    
# elif chr >= 97 and chr <= 122:
#     print("Lowercase Letter")
# elif chr >= 48 and chr <= 57:
#     print("Digit")
# else:
#     print("Special Character")

# for i in range(1, 11):
#     print(i*2)
  
# for i in range(1, 11):
#     for j in range(2, 11):
#         print(j * i, end="\t")
#     print()


# # Tables from 2 to 10
# for i in range(1, 11):
#     for j in range(2, 11):
#         print(j * i, end="\t")
#     print()

# print()

# # Tables from 11 to 20
# for i in range(1, 11):
#     for j in range(11, 21):
#         print(j * i, end="\t")
#     print()


#  for i in range(5, 0, -1):
#     print(i, end="\t ")

# print()

# for i in range(1, 6):
#     print(i, end="\t ")
# for i in range(5, 0, -1):
#     print(i, end=" ")

# print()

# for i in range(1, 6):
#     print(i, end=" ")

# for i in range(5, 0, -1):
#     print(i, "\t", 6 - i)
 

# for i in range(1, 6):
#     print(i, "\t", 6 - i)

print("Descending\tAscending")
print("-------------------------")

for i in range(5, 0, -1):
    print(i, "\t\t", 6 - i)

print("\nAscending\tDescending")
print("-------------------------")

for i in range(1, 6):
    print(i, "\t\t", 6 - i)      