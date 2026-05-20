# mytuple=("prashant","Ashish","sandip","komal","ankur","rajesh",23,3,15,77,"sandip")
# print(mytuple)
# print(type(mytuple))
# mytuple[2]="sunil"#TypeError: 'tuple' object does not support item assignment
# print(mytuple)


# mytuple=("prashant","Ashish","sandip","komal","ankur","rajesh",23,3,15,77,"sandip")

# print(mytuple)
# print(type(mytuple))

# # Convert tuple to list
# mylist = list(mytuple)

# # Modify value
# mylist[2] = "sunil"

# # Convert back to tuple
# mytuple = tuple(mylist)

# print(mytuple)

# init_tuple=()
# print(init_tuple.__len__())#0
# #A-None
# #B-1
# #C-0
# #D-Error


# init_tuple_a='a', 'b'
# init_tuple_b=('a', 'b')
# print(init_tuple_a==init_tuple_b)
# # A.0
# # B.1
# # C.false
# # D.true

# init_tuple_a='1', '2'
# init_tuple_b=('3', '4')
# print(init_tuple_a+init_tuple_b)#('1', '2', '3', '4`)
# #A.(1, 2, 3, 4)
# #B.('1', '2', '3', '4`)
# #C.['1', '2', '3', '4`]
# #D.NONE

# l=[1, 2, 3, 4]
# init_tuple=('Pythone',)*(l.__len__()-1[::-1][0])
# print(init_tuple)
# #A.()
# #B.('Pythone')
# #C.('Pythone', 'Pythone')
# #D. Runtime Exception


# init_tuple = ('Pythone',) * 3
# print(type(init_tuple))
# #A. <class 'str'>
# #B. <class 'tuple'>
# #C. <class 'list'>
# #D. <class 'int'>

# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)

# init_tuple = ((1,2),)*7
# print(len(init_tuple[3:8]))
# print(init_tuple[3:8])
# #A. Exception
# #B. 5
# #C. 4
# #D. None

# from ast import For


# mydict = {
#     101: "prashant",
#     102: "Ashish",
#     "103":"admin",
#     "104":"trivani ",
#     101:"ashish",
#     104:"asish"
# }
# print(mydict)

# # #with the help of keywe can print the value
# # a=mydict[102]
# # print(a)

# # #we will replACE the old value with new value by using key
# # mydict[102]="peter"
# # print(mydict)

# # #Printing keys by using keys() method
# # for x in mydict:
# #     print(x)

# #Printing values by using values() method
# # for x in mydict.values():
# #     print(x)

# # #Printing key and value by using items() method
# # for x, y in mydict.items():
# #     print(x, y)

# # #adding new key and value in the dictionary
# # mydict["Mobile_no"] = 1234567890
# # print(mydict)


# # #removing element from the dictionary by using pop keyword
# # mydict.pop(101)
# # print(mydict)

# # a = {(1,2):1,(2,3):2,(4,5):3,}
# # print(a[(4,5)])

# # a ={'a':1,'b':2,'c':3}
# # print(a['a','b'])
# # #A. key error
# # #B. [1,2]
# # #C. ('a':1, 'b':2)
# # #D. (1,2)

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)
# #A. 1
# #B. 2
# #C. 3
# #D. 4


# mydict = {}
# mydict[1] = 1
# mydict['1'] = 2
# mydict[1.0] = 4
# print(mydict)
# sum = 0
# for k in mydict:
#     sum += mydict[k]
# print(sum)
# #A. 7
# #B. Syntax Error
# #C. 3
# #D. 6

# mydict = {}
# mydict[(1,2,3,4)] = 8
# mydict[(4,2,1)] = 10
# mydict[(1,2)] = 12
# print(mydict)
# sum = 0
# for k in mydict:
#     sum += mydict[k]
# print(sum)
# #A. Syntax Error
# #B. 30 {(1, 2, 3, 4): 8, (4, 2, 1): 10, (1, 2): 12}
# #c. 47 {(1, 2, 3, 4): 8, (4, 2, 1): 10, (1, 2): 12}
# #D. 30{(1, 2): 12, (4, 2, 1): 10, (1, 2): 12}

# box = {}
# jars = {}
# crates = {}
# box['biscuits'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))
# #A. error


# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# rec = {"Name" : "Python", "Age" : 20,}
# r = rec.copy()
# print(id(r)==id(rec))
# print(id)

# def count_frequency(lst):
#     frequency = {}
#     for item in lst:
#         if item in frequency:
#             frequency[item] += 1
#         else:
#             frequency[item] = 1
#     return frequency

# numbers = [1, 2, 2, 3, 4, 3, 5]
# result = count_frequency(numbers)
# print(result)

