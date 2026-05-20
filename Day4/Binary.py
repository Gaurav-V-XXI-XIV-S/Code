# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums) - 1

#         while low <= high:
#             mid = (low + high) // 2

#             if nums[mid] == target:
#                 return mid

#             elif nums[mid] < target:
#                 low = mid + 1

#             else:
#                 high = mid - 1

#         return -1
#....................................................................#

#_____________________________Bubble Sort____________________________#
# def bubblesort(array):

#     for i in range(len(array) - 1):

#         for j in range(len(array) - i - 1):

#             if array[j] > array[j + 1]:

#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#                 print(array)
#             print()


# array = [64, 34, 25, 12, 22, 11, 90]

# bubblesort(array)
#....................................................................#


#_______________________Example______________________________________#
#to find security key

#1. Solution By Trainer
# mylist = [578378923]
# newlist = []

# for i in range(len(mylist)):
#     count=0
#     key=mylist[i]
#     j = i+1
#     while j<len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j = j+1
# print(len(newlist))

#2. Solution by Me
# n=input()
# count=0
# for i in range(10):
#     if n.count(str(i))>1:
#         count += 1
# if count ==0:
#     print(-1)
# else :
#     print(count)

#3. Solution By Chatgpt
# Input from user
# n = input("Enter a number: ")

# # Variable to store count
# count = 0

# # Check digits from 0 to 9
# for i in range(10):

#     # Count frequency of current digit
#     if n.count(str(i)) > i:
#         count += 1

# # Print result
# if count == 0:
#     print(-1)
# else:
#     print(count)
#............................................................................................#

#____________________________________________________________________________________________#
# class Student:
#     def __init__(self):
#         self.name = "Gaurav"
#         self.age = 22
    
#     def display(self):
#         print("Name=", self.name)
#         print("Age=", self.age)
# stuObj = Student()
# print(stuObj)
#.............................................................................................#

#_____________________________________________________________________________________________#
# class Message:
#     def __init__(self):
#         print("I am constructor")
#     def shows(self):
#         print("Class program")
# obj = Message()
#.............................................................................................#

#________________Basic Stack implementation in DSA_______________________#
# import sys
# class Stack:
#     def __init__(self):
#         self.myStack = []   #creating stack
    
#     def push(self, value):
#         self.myStack.append(value)
#         print("Element Push")
    
#     def display(self):
#         print(self.myStack)

# obj = Stack()
# print("Stack has created: ")
# while True:
#     print("1. Push operation: ")
#     print("2. Display Stack")
#     print("7. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice ==1:
#         value = int(input("Enter value to push in stack: "))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     else:
#         sys.exit()






#4_______________Stack Implimentation Without Size Limit_____________#
import sys
class Stack:
    def __init__(self):
        self.myStack = []   #creating stack
    
    def push(self, value):
        self.myStack.append(value)
        print("Element Push")
    
    def display(self):
        print(self.myStack)

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.myStack.pop())
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.myStack1[-1])

obj = Stack()
print("Stack has created: ")
while True:
    print("1. Push operation: ")
    print("2. Display Stack")
    print("3. Pop operation: ")
    print("4. peek operattion")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        value = int(input("Enter value to push in stack: "))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    else:
        sys.exit()