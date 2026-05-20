# String is a sequence of characters. It is a data type that is used to store text.
# In Python, strings are immutable, which means that they cannot be changed after they are created.
# Strings are defined by enclosing characters in quotes. 
# You can use single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """) to define a string.
# Triple quotes are used for multi-line strings.
# Here are some examples of strings in Python:
#.....................................................................................................................#
# name = "prashantjha"
# name = "prashantjha"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])
#----------------------------:------------------------------:---------------------------:----------------------------#



# string concatenation is the process of combining two or more strings into one string.
# In Python, you can concatenate strings using the + operator or the join() method.
# #.............................:..............................:...........................:...........................#
# s="Python are high level programming language"
# print(s.lower())#converting string to lower case
# print(s.upper())#converting string to upper case
# print(s.title())#converting string to title case
# print(s.capitalize())#converting string to capital case
# print(s.swapcase())#converting string to swap case
# print(s.count("a"))#counting number of occurrences of a character in a string
# print(s.find("a"))#finding the index of first occurrence of a character in a string
# print(s.rfind("a"))#finding the index of last occurrence of a character in a string
# print(s.replace("a","@"))#replacing a character in a string
# print(s.split())#splitting a string into a list of words
# print(s.split("a"))#splitting a string by a character
# print(s.strip())#removing leading and trailing whitespace from a string
# print(s.lstrip())#removing leading whitespace from a string
# print(s.rstrip())#removing trailing whitespace from a string
# print(s.startswith("Python"))#checking whether a string starts with a substring or not
# print(s.endswith("language"))#checking whether a string ends with a substring or not
#-----------------------------:------------------------------:---------------------------:----------------------------#

# name="prashant"
# sal = 5000
# age = 28
# print("{}sal is {} and age is {}".format(name,sal,age))#string formatting using format() method
# print("{0}sal is {1} and age is {2}".format(name,sal,age))#string formatting using format() method with positional arguments
# print("{x} sal is {y} and age is {z}".format(x=name,y=sal,z=age))#string formatting using format() method with keyword arguments
# A=1
# print(f"{A} is a good boy")#string formatting using f-string
 
# name="prashant"
# for i in name:
#     print(i)

# name="prashant"

# newname=""
# n = len(name)
# for i in range(n-1,-1,-1):
#     newname += name[i] 
#     print(newname)

#polindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# name="prashant"

# name = input("Enter a string: ")

# # Reverse the string
# rev = name[::-1]

# # Check palindrome
# if name == rev:
#     print("String is Palindrome")
# else:
#     print("String is Not Palindrome")
#......................................................................................................................#


# #Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# # Remove spaces and convert to lowercase
# str1 = str1.replace(" ", "").lower()
# str2 = str2.replace(" ", "").lower()

# # Check anagram
# if sorted(str1) == sorted(str2):
#     print("Strings are Anagrams")
# else:
#     print("Strings are Not Anagrams")

#count consonants and vowels in a string
# vowels = "a, e, i, o, u, A, E, I, O, U"
# name="hello"
# consonants=0
# for i in name:
#     if i in vowels:
#         continue
#     else:
#         consonants += 1
# print("Number of consonants:", consonants)
# print("Number of vowels:", len(name)-consonants)

# #count number of words in a string 
# name="hello world welcome to python programming."
# words = name.split()
# print("Number of words:", len(words))

# #count number of word and spaces in a string
# name="hello world welcome to python programming."
# words = name.split()
# spaces = name.count(" ")
# print("Number of words:", len(words))
# print("Number of spaces:", spaces)

# #count number of word and spaces in a string using loops
# name="hello world welcome to python programming."
# words = 0
# spaces = 0
# for i in name:
#     if i == " ":
#         spaces += 1
#     else:
#         words += 1
# print("Number of words:", words)
# print("Number of spaces:", spaces)

#count special characters in a string
# name="gasgg54@#vscs!ds*"
# special_characters = 0
# for i in name:
#     if i.isalnum():
#         continue
#     else:
#         special_characters += 1
# print("Number of special characters:", special_characters)

#pyra
import time
n=int(input("Enter a number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        time.sleep(0.5)
        print("*",end=" ")
    print()
   
