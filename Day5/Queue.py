# #In Queue we perform some Operations like 1. EnQueue, 2.DeQueue, 3. isEmpty, 4. display Queue, 5. isFull, 6. Delete(), 7. peek() 
# #Implementing Queue With Size
# # import sys

# # class Queue:

# #     def __init__(self, size):
# #         self.myQueue = []
# #         self.queueSize = size

# #     # Check Queue Full
# #     def isFull(self):
# #         if len(self.myQueue) == self.queueSize:
# #             return True
# #         else:
# #             return False

# #     # Check Queue Empty
# #     def isEmpty(self):
# #         if len(self.myQueue) == 0:
# #             return True
# #         else:
# #             return False

# #     # Enqueue Operation
# #     def enQueue(self, value):
# #         if self.isFull():
# #             print("Queue is Full")
# #         else:
# #             self.myQueue.append(value)
# #             print(value, "Inserted")

# #     # Dequeue Operation
# #     def deQueue(self):
# #         if self.isEmpty():
# #             print("Queue is Empty")
# #         else:
# #             removed = self.myQueue.pop(0)
# #             print(removed, "Removed")

# #     # Peek Operation
# #     def peek(self):
# #         if self.isEmpty():
# #             print("Queue is Empty")
# #         else:
# #             print("Front Element :", self.myQueue[0])

# #     # Display Queue
# #     def display(self):
# #         if self.isEmpty():
# #             print("Queue is Empty")
# #         else:
# #             print("Queue :", self.myQueue)

# #     # Delete Queue
# #     def Delete(self):
# #         self.myQueue.clear()
# #         print("Queue Deleted")


# # # Main Program

# # size = int(input("Enter the size of Queue : "))
# # obj = Queue(size)

# # print("Queue has been created")

# # while True:

# #     print("1. EnQueue Operation")
# #     print("2. Display Queue")
# #     print("3. DeQueue Operation")
# #     print("4. Peek Operation")
# #     print("5. Delete Queue")
# #     print("9. Exit")

# #     choice = int(input("Enter Your Choice : "))

# #     if choice == 1:
# #         value = int(input("Enter Value : "))
# #         obj.enQueue(value)

# #     elif choice == 2:
# #         obj.display()

# #     elif choice == 3:
# #         obj.deQueue()

# #     elif choice == 4:
# #         obj.peek()

# #     elif choice == 5:
# #         obj.Delete()
    
    
# #     elif choice == 9:
# #         print("Program Ended")
# #         sys.exit()

# #     else:
# #         print("Enter Valid Number")
# #......................................................................#

# #______________________________________________________________________#
# # fruit = {}
# # def addone(index):
# #     if index in fruit:
# #         druit[index] += 1
# #     else:
# #         fruit[index] = 1
# #     print(fruit)
# # addone('Apple')
# # addone('Banana')
# # addone('apple')
# # print(len(fruit))
# #.....................................................................#

# #_____________________Question to solve_______________________________#
# # write a program to accept student name and marks from the key board and creat dictionary. Also display student marks by tarcking student name 
# n = int(input("Enter the number of student: "))
# d = {}
# for i in range(n):
#     name = input("Enter Student Name:")
#     marks = input("Enter Student Marks:")
#     d[name] = marks
# while True:
#     name = input("Enter Student name to get Marks:")3
#     marks = d.get(name, -1)
#     if marks == -1:
#         print("Student Not Found")
#     else:
#         print("The Marks of", name , "are" , marks)
#     option = input("Do you want to find another student marks[Yes/No]")
#     if option == "No":
#         break
# print("Thanks for using our application")
# #..........................................................................#

# #__________________________________________________________________________#
# # s1, s2 = input().split()
# # missing = "NA"
# # for ch in s1:
# #     if ch not in s2:
# #         missing = ch
# #         break
# # print(missing)
# #..........................................................................#

# #__________________________________________________________________________#
# # x,y,z = map(int,input().split())
# # mylist = []
# # for i in rang (x):
# #     a = int(input())
# #     mylist.append(a)

# # for j in mylist:
# #     if j>y  and j<=z:
# #         print(j, end=' ')



# #___________________________________________________________________________#
# # import datetime

# # date = datetime.datetime.now()

# # print("Its Now: {:%d/%m/%y %H:%M:%S}".format(date))
# #...........................................................................#

# #___________________________________________________________________________#
# # x=['A','B','C']
# # y=['A','B','C']
# # z=[1,2,3,4]
# # print (x == y)
# # print (x == z)
# # print (x != z)
# #..........................................................................#

# #__________________________________________________________________________#
# # s=[1,4,9,16,25,36,49,64,81,100]
# # val = [2**i for i in range(1,6)]
# # print(val)
# #..........................................................................#
 
# #__________________________________________________________________________#
# # a,b = [int(x) for x in input ("Enter 2 numbers :").split()]
# # print("product is :",a*b)
# #..........................................................................#

# #__________________________________________________________________________#
# # a,b,c = [float(x)]



# #...........................................................................#
# import time
# class Tower:
#     def __init__(self): 
#         print("WELCOM TO TOWER OF HANOI GAME")
#         print()
#         print("GIven problem  A=[3,2,1]  B=[]    C[]")
#         print()
#         print("Expected Output A =[]  B=[]  C[3,2,1]")
#         self.A=[]
#         self.B=[]
#         self.C=[]
    
#     def tower(self, item):
#         self.A.append(item)
#         time.sleep(3)
#         print("A=",self.A)
#         print("Items in Tower A\n")
    
#     def pass1(self):
#         self.temp = self.A.pop(2)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
#         print("Pass one Completed=============================\n")

#     def pass2(self):
#         self.temp = self.A.pop(1)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
#         print("Pass 2 Completed=============================\n")
    
#     def pass3(self):
#         self.temp = self.C.pop(0)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
#         print("Pass 3 Completed=============================\n")

#     def pass4(self):
#         self.temp = self.A.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
#         print("Pass 4 Completed=============================\n")
    
#     def pass5(self):
#         self.temp = self.B.pop(1)
#         self.A.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
#         print("Pass 5 Completed=============================\n")

#     def pass6(self):
#         self.temp = self.B.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
#         print("Pass 6 Completed=============================\n")

#     def pass7(self):
#         self.temp = self.A.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
#         print("Pass 7 Completed=============================\n")

# obj = Tower()
# obj.tower(3)
# obj.tower(2)
# obj.tower(1)
# obj.pass1()
# obj.pass2()
# obj.pass3()
# obj.pass4()
# obj.pass5()
# obj.pass6()
# obj.pass7()