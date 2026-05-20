# # #Row wise max value
# #     # 0  1  2    3

# # # [0=[100, 198, 333, 323],

# # # 1=[122, 232, 221, 111],

# # # 2=[223, 565, 245, 764]]

# # newlist=[]
# # for i in range(3):#i=0
# #    j=0 #
# #    max = mylist[i][j] #[0][0]
# #    for j in range(4):
# #       c_max = mylist[i][j]
# #       if max c max:
# #       max = c max
# #     newlist.append(max)

# # print(newlist)


# # Row wise maximum value

# mylist = [
#     [100, 198, 333, 323],
#     [122, 232, 221, 111],
#     [223, 565, 245, 764]
# ]

# newlist = []

# for i in range(3):   # Loop through rows
#     j=0
#     max = mylist[i][j]   # Assume first element is maximum

#     for j in range(4):   # Loop through columns
#         c_max = mylist[i][j]

#         if c_max > max_val:
#             max_val = c_max

#     newlist.append(max_val)

# print(newlist)



# #input = 'prashant*is*a*good*Progarammer'
# #output = ****PrashantisgoodProgrammer
# name  = 'prashant*is*a*good*Progarammer'
# newname = ''
# val = ''
# for i in name:
#     if i !='*':
#         newname += i 
#     else:
#         val += i
# print(newname)
# print(str(val+newname))

#input = aaabbbbccceeeee
#output = a3b4c3e5


# name = 'aaabbbbccceeeee'
# result = ""
# count = 1
# for i in range(len(name)-1):
#     if name[i]==name[i+1]:
#       count += 1
#     else:
    
#         result += name[i] + str(count)
#         count = 1

 
# result += name[-1] + str(count)

# print(result)
#........................................................................................#

#_________________________________________________________________________________________#
salary = int(input('Enter your salary: '))
rating = float(input('Enter your performance appraisal rating: '))

increment = 0

if rating >= 1 and rating <= 3:
    increment = salary * 10 / 100

elif rating >= 3.1 and rating <= 4:
    increment = salary * 30 / 100

elif rating >= 4.1 and rating <= 5:
    increment = salary * 40 / 100

else:
    print('Invalid rating')

print('Incremented salary:', increment + salary)