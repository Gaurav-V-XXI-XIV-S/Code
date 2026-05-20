# mylist=["Gaurav","Abhay","Rohit","Vedant","Vinay","Dewang"]
# print(mylist)
# print(type(mylist))#<list>
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])
# print(mylist[-1])
# print(mylist[-2])
# print(mylist[-3])
# print(mylist[-4])
# print(mylist[-5])
# print(mylist[1:4])
# print(mylist[0:3])
# print(mylist[:3])
# print(mylist[2:])
# print(mylist[:])
# print(mylist[1:3:5])
# print(mylist[::2])

#changing value of list by using index
# mylist[0]="Gaurav Kumar"
# print(mylist)

# #checking whether "Gaurav" is present in the list or not by using "in" keyword
# if "Gaurav" in mylist:
#     print("Gaurav is present in the list")
# else:    
#     print("Gaurav is not present in the list")

# #aading new element in the list by using "append" method
# mylist.append("Vishakha")
# mylist.append("Rudransh")
# print(mylist)

# #inserting new element in the list by using "insert" method
# mylist.insert(2,"Rohit")
# print(mylist)

# #removing element from the list by using "remove" method
# mylist.remove("Rohit")
# print(mylist)

# #copying list by using "copy" method
# newlist=mylist.copy()
# print(newlist)


# mylist=[['gaurav','abhay'],[85,90],[80, "yyy"]]
# # print("Example of 2D list: ",mylist)
# # print(type(mylist))#<list> 
# # print("Accessing element of 2D list: ",mylist[0][0])#gaurav
# # print("Accessing element of 2D list: ",mylist[0][1])#abhay
# # print("Accessing element of 2D list: ",mylist[1][0])#85
# # print("Accessing element of 2D list: ",mylist[1][1])#90
# # print("Accessing element of 2D list: ",mylist[2][0])#80
# # print("Accessing element of 2D list: ",mylist[2][1])#"yyy"

# #removing element from 2D list by using "remove" method
# mylist.remove([85,90])
# print("After removing element from 2D list: ",mylist)

#removing element from 2D list by using "pop" method
# mylist.pop(0) 
#list1=[50,25,50,"Gaurav"]
# list1.clear()#removing all element from the list by using "clear" method
# print(list1)

# name="Gaurav"
# print(name)
# myname=list(name)
# print(myname)

#sorting list in ascending order by using "sort" method
# mylist=[5,3,8,1,2,4,7,6,9,0]
# mylist.sort()#sorting list in ascending order by using "sort" method
# print(mylist)

#variable assignment in list
# mylist=[5,3,8,1,2,4,7,6,9,0]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))

# #printing list by using for loop
# mylist=[5,3,8,1,2,4,7,6,9,0]
# for i in mylist:
#     print(i)

 #BY Chatgpt
# input_list = [0, 1, 4, 0, 2, 5]

# # Move zeros to the end
# result = [x for x in input_list if x != 0] + [0] * input_list.count(0)

# print(result)

# #By Trainer
# list1=[0, 1, 4, 0, 2, 5]
# for i in list1:
#     if i==0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)

# arr = [7, 3, 9, 2, 8]

# arr.sort()

# second_largest = arr[-2]

# print("Second Largest Element is:", second_largest)

# #ValueError: attempt to assign sequence of size 6 to extended slice of size 5
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)


# a=[1,2,3,4,5]
# print(a[3:0:-1])

# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# arr =[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]

# for i in range(0,6):
#     print(arr[i],end=" ")


# fruit_list1=["apple","Berry","Cherry","papaya"]
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]="Gaava"
# fruit_list3[1]="kivi"

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == "Gaava":
#         sum += 1    
#     if ls[1]=="kivi":
#         sum += 20
# print(sum)