#_______________________________Linked List Solution_____________________________#
#
# import sys

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def addNode(self, value):
#         self.node = Node(value)

#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.tail.next = self.node
#             self.tail = self.node

#     def addatbegin(self, value):
#         print("add node begining")

#         self.node = Node(value)

#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.node.next = self.head
#             self.head = self.node

#     def addbetween(self, value, position):
#         print("add node in between")

#         self.node = Node(value)

#         if self.head is None:
#             print("Linkedlist is empty")
#             return

#         temp = self.head
#         count = 1

#         while count < position - 1 and temp is not None:
#             temp = temp.next
#             count += 1

#         if temp is None:
#             print("Invalid Position")
#         else:
#             self.node.next = temp.next
#             temp.next = self.node

#             if self.node.next is None:
#                 self.tail = self.node

#             print("Node inserted successfully")

#     def addatend(self, value):
#         print("add node at end")

#         self.node = Node(value)

#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.tail.next = self.node
#             self.tail = self.node

#     def display(self):

#         if self.head is None:
#             print("Linkedlist is empty")
#             return

#         temp = self.head

#         while temp is not None:
#             print(temp.data, "|", "->", end=" ")
#             temp = temp.next

#         print("None")


# if __name__ == '__main__':

#     object = Linkedlist()

#     while True:

#         print("\n1.Add node in linkedlist")
#         print("2.Add node in begining")
#         print("3.Add node in between")
#         print("4.Add node in End")
#         print("5.Display Linkedlist")
#         print("6.Exit")

#         ch = int(input("enter your choice:"))

#         if ch == 1:

#             value = int(input("enter value for node:"))
#             object.addNode(value)

#             print("Node Successfully Added in single linkedlist:")

#         elif ch == 2:

#             value = int(input("enter value for node:"))
#             object.addatbegin(value)

#         elif ch == 3:

#             value = int(input("enter value for node:"))
#             position = int(input("Enter position:"))

#             object.addbetween(value, position)

#         elif ch == 4:

#             value = int(input("enter value for node:"))
#             object.addatend(value)

#         elif ch == 5:

#             object.display()

#         elif ch == 6:

#             sys.exit()

#         else:
#             print("Invalid Choice")
#..............................................................................#

#_______________________________Factorial Solution_____________________________#

# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# print(factorial(4))
#...............................................................................#

#_______________Capitalize the first solution using recursion___________________#
# def capitalizefirst(arr): #define a function which takes an array as input

#     result = []# create an empty array to store the capitalized strings
#     if len(arr) == 0:# check if the input array is empty
#         return result# if the array is empty, return the empty result array
    
#     result.append(arr[0][0].capitalize()+arr[0][1:])# capitalize the first character of the first string in the array and append it to the result array, while keeping the rest of the string unchanged
#     return result + capitalizefirst(arr[1:])# recursively call the function with the rest of the array (excluding the first element) and concatenate the result with the current result array

# print(capitalizefirst(['gaurav', 'sachin', 'rohit']))# Output: ['Gaurav', 'Sachin', 'Rohit']
#...............................................................................#

#_______________________________Produt of Array_________________________________#
# def productofArray(arr):# define a function that takes an array as input
#     if len(arr) == 0:# check if the input array is empty
#         return 1# if the array is empty, return 1 (the identity for multiplication)
#     else:# if the array is not empty, return the product of the first element and the result of recursively calling the function with the rest of the array (excluding the first element)
#         return arr[0] * productofArray(arr[1:])# recursively call the function with the rest of the array (excluding the first element)
    
# print(productofArray([1, 2, 3, 4]))# Output: 24
# #...............................................................................#

# #____________________________Reverse a String_________________________________#
# #in recursion
# def reverseString(s):
#     if len(s) == 0:# check if the input string is empty
#         return ""# if the string is empty, return an empty string
#     else:# if the string is not empty, return the last character of the string concatenated with the result of recursively calling the function with the rest of the string (excluding the last character)
#         return s[-1] + reverseString(s[:-1])# recursively call the function with the rest of the string (excluding the last character)

# print(reverseString("hello"))# Output: "olleh"   
#...............................................................................#

#__________________________________By sir_______________________________________#
def reverse(string):# define a function that takes a string as input
    if len(string) <= 1:# check if the input string has a length of 1 or less
        return string# if the string has a length of 1 or less, return the string itself (base case for recursion)
    return string[len(string) - 1] + reverse(string[:len(string) - 1])# return the last character of the string concatenated with the result of recursively calling the function with the rest of the string (excluding the last character)

print(reverse("Python"))# Output: "nohtyP"
print(reverse("appmillers"))# Output: "srellimppa"