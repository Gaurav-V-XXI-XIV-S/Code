# # import re 
# # count = 0
# # matcher = re.finditer("Hi","HiHiHiHi")

# # for i in matcher:
# #     count += 1
# #     print(i.start(),"...",i.end(),"...",i.group())
# # print("Total number of matches:", count)
# #...................................................................#


# #___________________________________________________________________#
# # import re

# # mtch = re.finditer('[A-Z]', 'abch3hdhjhdjhdhH')

# # for i in mtch:
# #     print(i.start(), "...", i.end(), "...", i.group())
# #...................................................................#

# #___________________________________________________________________#
# # import re
# # obj = re.sub('[a-z]','*','2345 ABCD habc defg')
# # print(obj)
# #...................................................................#

# #___________________________________________________________________#
# # import re

# # obj = re.subn('[0-7]', '*', 'ab3gd6nk17')

# # print(obj)
# # print("the string is =", obj[0])
# # print("the number of replacement is =", obj[1])
# #...................................................................#

# #___________________________________________________________________#
# # import re
# # f1 = open("file1.txt", "r")
# # f2 = open("file2.txt", "w")
# # for line in f1:
# #     obj = re.sub('a', '*', line)
# #     f2.write(obj)
# #....................................................................#



# #____________________________________________________________________#
# # import re
# # count=0
# # pattern=re.compile("Buch")
# # matcher=pattern.finditer("Buch kli mli pli sili")
# # for i in matcher:
# #     count+=1
# #     print(i.start(),"...",i.end(),"...",i.group())
# # print("The number of occurrences: ", count)
# #....................................................................#


# #____________________________________________________________________#
# # import re
# # count=0
# # matcher=re.finditer("Hi","HihihihiHihihiHi")
# # for i in matcher:
# #     count+=1
# #     print(i.start(),"...",i.end(),"...",i.group())
# # print("The number of occurrences: ",count)
# #....................................................................#



# #_____________________________________________________________________#
# # import re
# # obj=input("Enter any character: ")
# # objmatch=re.finditer(obj,"a7b *@fahsaf")
# # for match in objmatch:
# #     print(match.start(),"...",match.end(),"...",match.group())
# #....................................................................#


# #_____________________________________________________________________#
# # import re
# # a=input("Enter string to perform match operation: ")
# # mach=re.match(a,"Python is very important language")#match is used to find starting or ending of a file it returns true or false
# # print(mach)
# # if mach!=None:
# #     print("match found at the beginning level")
# #     print(mach.start()," ",mach.end())
# # else:
# #     print("there is no matching at beginning level")
# #....................................................................#



# #_____________________________________________________________________#    
# # import re
# # a=input("Enter string to perform match operation: ")
# # mach=re.fullmatch(a,"Python is veryimportantlanguage")#matchfull- agar pura match hota hai toh object return otherwise none
# # print(mach)
# # if mach!=None:
# #     print("match found")
# #     print(mach.start()," ",mach.end())
# # else:
# #     print("Fullmatch not found")
# #....................................................................#


# #_____________________________________________________________________#
# #A PROGRAM TO CHECK WHETHER MAIL IS VALID

# # import re
# # s=input("Enter mail id: ")
# # m=re.fullmatch("\\w[a-zA-Z0-9_.]*@gamil[.]com",s)
# # if m!=None:
# #     print("Valid E-mail ID")
# # else:
# #     print("Invalid EE-Mail ID")
# #....................................................................#


# #_____________________________________________________________________#
# #A PROGRAM TO CHECK WHETHER MOBILE NUMBER IS VALID
# # import re
# # mo=input("Enter mobile number: ")
# # obj=re.fullmatch("\\+[1-9]{1}[0-9]\\d{9}",mo)
# # if obj!=None:
# #     print("Valid mobile number")
# # else:
# #     print("Invalid number")
# #....................................................................#



# #_____________________________________________________________________#
# #A PROGRAM TO CHECK WHETHER PASSWORD IS VALID
# # import re
# # a=input("Enter string to perform match operation: ")
# # mach=re.search(a,"Python is veryimportantlanguage")
# # print(mach)
# # if mach!=None:
# #     print("match found")
# #     print(mach.start()," ",mach.end()," ",mach.group())
# # else:
# #     print("There is no matching anywhere")
# #....................................................................#


# #_____________________________________________________________________#
# #
# # import re
# # mtch=re.findall('[0-9a-z]',"abch4567ASDFYUIKLdhdshag57d&*($)")
# # print(mtch)
# #....................................................................#



# #_____________________________________________________________________#

# # import re
# # obj=re.sub('[a-z]','*','2345 ABCA defsads')
# # print(obj)
# #....................................................................#



# #_____________________________________________________________________#
# #
# # import re
# # obj=re.subn('[0-7]','@','ab3dfs56')
# # print(obj)
# # print("The string is= ",obj[0])
# # print("The sumber of replacement is",obj[1])
# #....................................................................#


# #_____________________________________________________________________#
# reg   searc
import re
import os

# Show current working directory
print("Current Working Directory:", os.getcwd())

try:
    # Open input file
    with open("para.txt", "r") as f1:

        # Read file content
        text = f1.read()

    # Take user input
    mach = input("Enter text to search: ")

    # Find all matches
    matches = re.finditer(mach, text)

    found = False

    # Open output file
    with open("output.txt", "w") as f2:

        for m in matches:
            found = True

            result = (
                f"Match found: {m.group()} "
                f"Start Index: {m.start()} "
                f"End Index: {m.end()}\n"
            )

            print(result)

            # Write into output file
            f2.write(result)

    if not found:
        print("No Match Found")

except FileNotFoundError:
    print("Error: para.txt file not found.")
    print("Create para.txt in the same folder as this Python file.")
#....................................................................#


#______________________________________________________________________#
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