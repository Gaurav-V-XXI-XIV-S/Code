# # #4_______________Stack Implimentation Without Size Limit_____________#
# # import sys
# # class Stack:
# #     def __init__(self):
# #         self.myStack = []   #creating stack
    
# #     def push(self, value):
# #         self.myStack.append(value)
# #         print("Element Push")
    
# #     def display(self):
# #         print(self.myStack)

# #     def isEmpty(self):
# #         if self.myStack == []:
# #             return True
# #         else:
# #             return False
        
# #     def pop(self):
# #         if self.isEmpty():
# #             print("stack is empty")
# #         else:
# #             print(self.myStack.pop())
# #     def peek(self):
# #         if self.isEmpty():
# #             print("Stack is empty")
# #         else:
# #             print(self.myStack1[-1])

# # obj = Stack()
# # print("Stack has created: ")
# # while True:
# #     print("1. Push operation: ")
# #     print("2. Display Stack")
# #     print("3. Pop operation: ")
# #     print("4. peek operattion")
# #     print("7. Exit")
# #     choice = int(input("Enter your choice: "))
# #     if choice ==1:
# #         value = int(input("Enter value to push in stack: "))
# #         obj.push(value)
# #     elif choice == 2:
# #         obj.display()
# #     elif choice == 3:
# #         obj.pop()
# #     elif choice == 4:
# #         obj.peek()
# #     else:
# #         sys.exit() 


# # Stack Implementation With Size Limit Using Python

# import sys


# class Stack:

#     # Constructor
#     def __init__(self, size):

#         self.myStack = []      # Creating stack
#         self.size = size       # Maximum size of stack

#     # Push Operation
#     def push(self, value):

#         if self.isFull():

#             print("Stack Overflow")

#         else:

#             self.myStack.append(value)

#             print(value, "Inserted Into Stack")

#     # Pop Operation
#     def pop(self):

#         if self.isEmpty():

#             print("Stack Underflow")

#         else:

#             deleted = self.myStack.pop()

#             print(deleted, "Deleted From Stack")

#     # Peek Operation
#     def peek(self):

#         if self.isEmpty():

#             print("Stack is Empty")

#         else:

#             print("Top Element:", self.myStack[-1])

#     # Display Operation
#     def display(self):

#         if self.isEmpty():

#             print("Stack is Empty")

#         else:

#             print("\nStack Elements:")
                 
#             for i in reversed(self.myStack):

#                 print(i)

#     # Check Stack Empty
#     def isEmpty(self):

#         if len(self.myStack) == 0:

#             return True

#         else:

#             return False

#     # Check Stack Full
#     def isFull(self):

#         if len(self.myStack) == self.size:

#             return True

#         else:

#             return False

#     # Delete Entire Stack
#     def deleteStack(self):

#         self.myStack = []

#         print("Entire Stack Deleted Successfully")


# # Take stack size from user
# size = int(input("Enter Stack Size: "))

# # Object creation
# obj = Stack(size)

# print("\nStack Created Successfully")


# # Menu Driven Program
# while True:

#     print("\n========== STACK MENU ==========")

#     print("1. Push Operation")
#     print("2. Pop Operation")
#     print("3. Peek Operation")
#     print("4. Display Stack")
#     print("5. Check Stack Empty")
#     print("6. Check Stack Full")
#     print("7. Delete Entire Stack")
#     print("8. Exit")

#     choice = int(input("Enter Your Choice: "))

#     # Push
#     if choice == 1:

#         value = int(input("Enter Value To Push: "))

#         obj.push(value)

#     # Pop
#     elif choice == 2:

#         obj.pop()

#     # Peek
#     elif choice == 3:

#         obj.peek()

#     # Display
#     elif choice == 4:

#         obj.display()

#     # Check Empty
#     elif choice == 5:

#         if obj.isEmpty():

#             print("Stack is Empty")

#         else:

#             print("Stack is Not Empty")

#     # Check Full
#     elif choice == 6:

#         if obj.isFull():

#             print("Stack is Full")

#         else:

#             print("Stack is Not Full")

#     # Delete Stack
#     elif choice == 7:

#         obj.deleteStack()

#     # Exit
#     elif choice == 8:

#         print("Program Exited Successfully")

#         sys.exit()

#     # Invalid Choice
#     else:

#         print("Invalid Choice")


       