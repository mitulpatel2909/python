
# string  type 

# 1 : 'test string'
# 2 : "test string"
# 3 : """test string"""


# =============

# name = "my name is python"
# print(type(name))
# print(name)

# ===========

# string indexing and slicing 
# index start in 0 number

# name = "my name is python"

# print(name[0])
# print(name[1])
# print(name[2])

# print(name[-2])



# print(name[0:2],end="")
# print(name[8:10], end="" )

# print(name[:10])
# print(name[4:])
# print(name[:])

# print(name[0:10:1])

# =================

# string function and method 

# name = "my name is python"

"""""""""""""""""""""""
1 : len : The len() function returns an integer representing the total number of characters in the provided string. 

2 : upper : return a copy of the string with all cased characters converted to uppercase

3 : lower : return a copy of the string with all cased characters converted to lowercase

4 : title : Returns a titlecased version of the string, where words start with an uppercase character and the remaining characters are lowercase.

5 : isupper : Returns True if all cased characters in the string are uppercase and there is at least one cased character.

6 : islower :  Returns True if all cased characters in the string are lowercase and there is at least one cased character.

7 : istitle : The istitle() method in Python is a built-in string method used to check if a string adheres to the rules of a title-cased string. It returns True if the string is title-cased and contains at least one character, otherwise, it returns False.
 
8 : isdigit :  Returns True if all characters in the string are digits, and there is at least one character

9 : capitalize :Returns a copy of the string with only its first character capitalized.

10 : center :  Returns a centered string of a specified width, padded with fillchar.

11 : startswith :  Returns True if the string starts with the specified prefix, otherwise False.

12 : endswith : Returns True if the string ends with the specified suffix, otherwise False.

13 : count : Returns the number of non-overlapping occurrences of substring. 

14 : index : Similar to find(), but raises a ValueError if substring is not found.

15 : find : Returns the lowest index in the string where substring is found. Returns -1 if not found.

16 : replace : Returns a copy of the string with all occurrences of old replaced by new.

17 : ord : The ord() function in Python is a built-in function that takes a single Unicode character as a string argument and returns its integer Unicode code point value.

18 : chr : The chr() function in Python is a built-in function that returns a string representing a character whose Unicode code point is the integer provided as an argument. 

"""""""""""""""""

# 1 : len :

# name="my name is python "
# print(len(name))

# 2 : upper :

# name="my name is python "
# print(name.upper())

# 3 : lower :

# name="MY NAME IS PYTHON"
# print(name.lower())

# 4 : title :

# name="my name is python "
# print(name.title())

# 5 : isupper :

# name="MY NAME IS PYTHOn"
# print(name.isupper())


# 6 : islower :

# name="my name is python N "
# print(name.islower())


# 7 : istitle :

# name="My Name Is Python"
# print(name.istitle())

# 8 : isdigit :

# name="123231"
# print(name.isdigit())


# 9 : capitalize : 
# name="my name is python"
# print(name.capitalize())


# 10 : center :
# name="python"
# print(name.center(3,"*"))


# 11 : startswith :

# name="my name is python"
# print(name.startswith("my n"))

# 12 : endswith :

# name="my name is python"
# print(name.endswith("thon"))

# 13 : count :
# name="my name is python"
# print(name.count("my"))


# 14 : index :

# name="my name is python"
# print(name.index("i"))

# 15 : find :
# name="my name is python"
# print(name.find("z"))

# 16 : replace :
# name="my name is python django python"
# print(name.replace("my","php"))

# 17 : ord :


# print(ord("a"))
# print(ord("z"))

# print(ord("A"))
# print(ord("Z"))

# 18 : chr :

# print(chr(65))
# print(chr(66))



# ==============================


# name="my name is python"
# for i in name:
#     print(i)


# name="my name is python"
# for i in range(len(name)):
#     print(i,name[i])

# ====================== A To Z Print =================

# for i in range(65,91):
#     print(chr(i),end=" ")
# print()    
# for i in range(97,123):
#     print(chr(i),end=" ")

# Aa Bb

# for i in range(65,91):
#     print(f"{chr(i)}{chr(i+32)}",end=" ")


# ==============================

# Task 1: 
# name = "my name is python"
# output : mynameispython

# name = "my name is python "
# print(name.replace(" ",""))


# Task 2 : 
# name = "my name is python"
# output  : count m    without count function

# name = "my name is python"
# a = 0

# for i in name:
#     if i == 'm':
#         a += 1
# print(a)


# Task : 3 :
# name = "my name is python"
# output : my$name$is$python without replace function

# name = "my name is python"

# a = ""

# for i in name:
#     if i == " ":
#         a += "$"
#     else:
#         a += i
# print(a)


# Task : 4 
# name = "mitul"
# ouput : "MITUL" without upper function 

# name = "mitul  python"

# name1=""
# for i in name:
#     if i == " ":
#         name1 += " "
#     else:    
#         name1+=chr(ord(i)-32)
# print(name1)



