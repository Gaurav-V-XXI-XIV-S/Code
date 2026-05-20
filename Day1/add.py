# #Why python is called dynamic typed language? it has both compiler and interpreter 
# age=22
# pi = 3.14
# name="John"
# result= True
# print(type(age))
# print(type(pi))
# print(type(name))   
# print(type(result))
# #checking address by using "ID" key
# print(id(age))
   
# ############################reverse a number############################
# num = 123
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# rev = a*100 + b*10 + c
# print(rev)
# #1233456 == 654321


#####################Palindrome Number#####################
# num = 12321
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = num // 10
# e = num % 10
# num = num // 10
# rev = a*10000 + b*1000 + c*100 + d*10 + e
# if rev == 12321:
#     print("Palindrome Number")
# else:
#     print("Not Palindrome Number")


##############Palindrome number by using loops#####################
# num = 12321
# rev = 0
# while num > 0:
#     a = num % 10
#     rev = rev * 10 + a
#     num = num // 10
# if rev == 12321:
#     print("Palindrome Number")
# else:
#     print("Not Palindrome Number")    


####################Currancy check how many notes of 100, 50, 20, 10, 5, 2, 1 are required to make the given amount#####################
# Amount = int(input("Enter the amount: "))
# print("Number of 100 notes:", (Amount // 100))
 
# print("Number of 50 notes:", (Amount % 100) // 50)
 
# print("Number of 20 notes:", ((Amount % 100)%50) // 20)
 
# print("Number of 10 notes:",(((Amount % 100)%50)%20) // 10)
 
# print("Number of 5 notes:", (((Amount % 100)%50)%20) // 5)
  
# #find for 2 notesand 1 notes
# print("Number of 2 notes:", Amount // 2)
 
# print("Number of 1 notes:", Amount) 



######################################counting Note ##################
# Amount = int(input("Enter the amount: "))

# print("100 notes:", Amount // 100)
# print("50 notes:", (Amount % 100) // 50)
# print("20 notes:", (Amount % 50) // 20)
# print("10 notes:", (Amount % 20) // 10)
# print("5 notes:", (Amount % 10) // 5)
# print("2 notes:", (Amount % 5) // 2)
# print("1 notes:", (Amount % 2))