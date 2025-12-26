

# d1 = {
#     "python":"django",
#     1:2,
#     1.5:5
# }
# print(d1)
# print(type(d1))


# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# print(d1)
# print(d1["name"])
# print(d1["age"])



# dictionary function and method 

# 1 : len : The len() function in Python, when used with a dictionary, returns the number of key-value pairs (items) present in that dictionary.

# 2 : keys :  Returns a view object that displays a list of all the keys in the dictionary.

# 3 : values :  Returns a view object that displays a list of all the values in the dictionary.

# 4 : items : Returns a view object that displays a list of a dictionary's key-value tuple pairs.

# 5 : pop : Removes the item with the specified key and returns its value. If the key is not found and default_value is not provided, a KeyError is raised.

# 6 : popitem : Removes and returns the last inserted key-value pair as a tuple.

# 7 : clear : Removes all items from the dictionary.

# 8 : get : Returns the value for the specified key. If the key is not found, it returns None by default, or the default_value if provided.

# 9 : update : Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.


# 1 : len :

# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# print(len(d1))


# 2 : keys :

# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# print(d1.keys())


# 3 : values :

# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# print(d1.values())

# 4 : items :


# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# print(d1.items())

# 5 : pop :


# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# d1.pop("python")
# print(d1)

# 6 : popitem :

# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# d1.popitem()
# print(d1)

# 7 : clear :


# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# d1.clear()
# print(d1)

# 8 : get :


# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# print(d1.get("python"))
# print(d1)

# 9 : update :


# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }

# d1.update({1:2})
# print(d1)

# d1 = {
#     "python":"django",
#     "name":"mitul",
#     "age":21,
#     "subject":"dict"
# }
# d2={
#     1:2,
#     3:4,
#     5:6
# }

# d1.update(d2)
# print(d1)


# nested dictionary 

# student = {
#     "name": "Alice",
#     "age": 20,
#     "grades": {
#         "math": 88,
#         "science": 92,
#         "history": 79
#     },
#     "address": {
#         "city": "New York",
#         "zip": "10001"
#     }
# }

# print(student.keys())
# print(student.values())

# print(student["address"].keys())
# print(student["address"].values())


# ==================

# Task : 1 

# l1=[1,2,3,4,5]
# l2=[11,12,13,14,15]
# l2.reverse()
# for i in range(1,6): 
    
# a = dict(zip(l1,l2))
# print(a)


# print(f"{n}:{i}", end=" ")

# output : {1:15,2:14,3:13,4:12,5:11} 

# Task : 2

# d1 = {1:15,2:14,3:13,4:12,5:11} 

# print(d1.keys())
# a = d1.keys()
# print(sum(a))

# print(d1.values())
# b = d1.values()
# print(sum(b))

# key sum = 1+2+3+4+5=
# values sum = 15+14+13+12+11=

# =====================================


# Task : 3 : Que Task 

# Q1 : 10+10 
# Q2 : 15-7
# Q3 : 23*5
# Q4 : 28/4
# Q5 : 11*11
# Q6 : 7**3
# Q7 : 9//2
# Q8 : 11==11
# Q9 : 15>3
# Q10 :27<56

# ch a que number : 3
# Q3 : 10*10 
# A : 20
# B : 30
# C : 100
# D : 200
# E : None


l1 = ["10+10","15-7","23*5","28/4","11*11","7**3","9//2","11==11","15>3","27<5"]
# l2=[{"A":20},{"B":8},{"C":115},{"D":7},{"E":121},{"F":343},{"G":4},{"H":True},{"I":True},{"J":False},{"K":None}] 

for i in range(len(l1)):
    print(f"Q{i+1}",l1[i])


# for n in range(len(l2)):
    # print(l2[n])

    
q_input=int(input("Enter A Que Number : "))
if q_input>len(l1):
    print("None")
else:
    result = eval(l1[q_input-1])
    # result = l2[n-1]
    print(f"Q{q_input}",l1[q_input-1])
    # print("evaluated ans:",result)
    # print("l2[n]:",result)

# for n in range(len(l2)):
#     print(l2[n])

l2=[{"a":20},{"b":15},{"c":5},{"d":None}]
for b in range(len(l2)):
    print(l2[b])

b = result
print(b)

if b==20:
    print({"A":20})
