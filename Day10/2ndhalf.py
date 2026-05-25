#___________________REGULAR EXPRESSION__________________
# import re  #remodule for performing all the regular expression based operation
# count =0
# pattern = re.compile("function")

# matcher = pattern.finditer("A function in pytho is defined by a def statement. python the general syntax looks like this: def function-name(Parameter list): statements, i.e the function body. The parameter python list consist of none or more parameters")

# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
#     print("The number of occurences:",count)







#=============================================================================================
# import re
# count = 0
# matcher = re.finditer("Hi","HiHiHiHi")
# for i in matcher:
#     count += 1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences: ",count)






#-------------------------------------------------------------------------------------------
# import re
# obj = input("enter any character: ")
# objmatch = re.finditer(obj,"a7b @k9z")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())






#===========================================================================================
#_______________match() function_________________________
# import re
# a = input("Enter string to perform match operation: ")
# mtch = re.match(a,"python is very important languuage")
# print(mtch)

# if mtch!=None:
#     print("match found at begining level")
#     print(mtch.start(), " ",mtch.end())
# else:
#     print("there is no matching at beginning level")







#------------------------------------------------------------------------------
#____________ fullmatch() _____________
# import re
# a = input("Enter string to perform match operation: ")
# mtch = re.fullmatch(a,"pythonisvery")
# print(mtch)

# if mtch!=None:
#     print("match found")
#     print(mtch.start(), " ",mtch.end())
# else:
#     print("Full match not found")






#-------------------------------------------------------------------
#WAP to python program to check whether the given mail is valid or not?

# import re
# s = input("Enter Mail id: ")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail.com",s)
# if m!= None:
#     print("Valid E-mail ID")
# else:
#     print("Invalid E-Mail ID")







# #WAP to check the valid mobile number
# import re
# mo = input("Enter mobile number: ")
# obj = re.fullmatch("[0-5]\d{9}",mo)
# if obj!= None:
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")






# #____ search() function _______--
# import re
# a = input("Enter string to perform match operation: ")
# mtch = re.search(a,"python isssssss dynamic lannn")
# print(mtch)

# if mtch!=None:
#     print("match found")
#     print(mtch.start(), " ",mtch.end()," ",mtch.group())
# else:
#     print("There is no matching anywhere")







# #---------findall() function-------------
# import re
# mtch = re.findall('[A-Z]',"abch3hdh5bk72Q$Z&*")
# print(mtch)






#====================================================================
# # #---------sub() function-------------
# import re
# obj = re.sub('[a-z]','*','2345 ABCD habc deff')
# print(obj)






#==================================================================
# # #---------subn() function-------------
# import re
# obj = re.sub('[0-7]','@','ab3gd6nk17')
# print(obj)
# print("the string is=", obj[0])
# print("the number of replacement is=",obj[1])







# #=================================================================
# #regression 
# import re
# import os

# # Show current working directory
# print("Current Working Directory:", os.getcwd())

# try:
#     # Open input file
#     with open("para.txt", "r") as f1:

#         # Read file content
#         text = f1.read()

#     # Take user input
#     mach = input("Enter text to search: ")

#     # Find all matches
#     matches = re.finditer(mach, text)

#     found = False

#     # Open output file
#     with open("output.txt", "w") as f2:

#         for m in matches:
#             found = True

#             result = (
#                 f"Match found: {m.group()} "
#                 f"Start Index: {m.start()} "
#                 f"End Index: {m.end()}\n"
#             )

#             print(result)

#             # Write into output file
#             f2.write(result)

#     if not found:
#         print("No Match Found")

# except FileNotFoundError:
#     print("Error: para.txt file not found.")
#     print("Create para.txt in the same folder as this Python file.")








# #_____________________________________________________________________________________________________
# # Program to print the number of lines, words,
# # and characters present in a file

# import os
# import sys

# fname = input("Enter File Name: ")

# # Check file exists or not
# if os.path.isfile(fname):

#     print("File exists:", fname)

#     f = open(fname, "r")

# else:
#     print("File does not exist:", fname)
#     sys.exit(0)

# # Initialize counters
# lcount = 0
# wcount = 0
# ccount = 0

# # Read file line by line
# for line in f:

#     # Count lines
#     lcount = lcount + 1

#     # Count characters
#     ccount = ccount + len(line)

#     # Count words
#     words = line.split()
#     wcount = wcount + len(words)

# # Print results
# print("The number of Lines:", lcount)
# print("The number of Words:", wcount)
# print("The number of Characters:", ccount)

# f.close()








# #------------------------------------------------------------------------------------------------------
# class Graph:

#     def __init__(self, vertices):
#         self.V = vertices
#         self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

#     def add_edge(self, u, v):
#         self.matrix[u][v] = 1
#         self.matrix[v][u] = 1   # Undirected graph

#     def display(self):

#         for row in self.matrix:
#             print(row)

#     def remove_edge(self, u, v):
#         if self.matrix[u][v] == 0:
#             print("No edge exists between", u, "and", v)
#             return

#         self.matrix[u][v] = 0
#         self.matrix[v][u] = 0
#         print("Edge removed successfully")


# g = Graph(4)

# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 3)

# print("Adjacency Matrix:")
# g.display()
# g.remove_edge(0, 2)
# print("\nMatrix After Removing Edge:")
# g.display()
#======================================================================#







# #Hash
# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def hash_function(self, key):
#         return key % self.size
    
#     def insert(self, key):
#         index = self.hash_function(key)
#         self.table[index].append(key)

#     def display(self):
#         print(self.table)

# h = HashTable(10)
# h.insert(15)
# h.insert(25)
# h.insert(35)
# h.display()