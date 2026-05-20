# arr = [1,1,0,1,1,1,0,1,1,1,1]

# current_count = 0
# max_count = 0

# for num in arr:
#     if num == 1:
#         current_count += 1
#         if current_count > max_count:
#             max_count = current_count
#     else:
#         current_count = 0

# print("Maximum consecutive 1s:", max_count)

#................................................................................................#


#_______________________________Count Substring in a String______________________________________#
# string = "abababab"
# substring = "ab"

# count = 0

# for i in range(len(string) - len(substring) + 1):
#     if string[i:i+len(substring)] == substring:
#         count += 1

# print("Count:", count)

#................................................................................................#

#_____________________________While Loop_________________________________________________________#
# i = 1
# while i<=5:
#     print(i)
#     i+= 1

#................................................................................................#

#____________________________________Function____________________________________________________#
# def hello():
#     print("hello world")

# hello() # calling function
# hello()
#.................................................................................................#

#___________________________________Linear Search_________________________________________________#
# def linearsearch(array, target):
#     for i in range(0, len(array)):
#         if array[i] == target:
#             return i 
#         return -1
        
# array = [1,2,3,4,9,7,9]
# target = 0 
# result = linearsearch(array, target)
# if result == -1:
#     print("Target Value not found")
# else:
#     print("Target value at index",result)
#.................................................................................................#
 
#_________________Removing Space from string______________________________________________________#
# city=input("Enter your city Name:")
# scity=city.strip()
# if scity=='Hydrabad':
#     print("Hello Hydrabadi...adab")
# elif scity=='Chennai':
#     print("Hello Madrasi...Vanakkam")
# elif scity=='banglore':
#     print("Hello Kannadiga...Shubhodaya")
# else:
#     print("Your Entered City Is Invalid")

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def compareTriplets(a, b):
#     # Write your code here
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
