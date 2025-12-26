

# s1 = {1,2,3,4,5,6,7,8,9,10}
# print(s1)
# print(type(s1))



# s1 = {1,2,3,4,1,3,2,6,5,6,7,8,9,10}
# print(s1)


# s1 = {1,2,3,4,1,3,2,6,5,6,7,8,9,10}
# print(s1[3])


# ===============================

# s1 = {}
# print(s1)
# print(type(s1))


# s1 = set()
# print(s1)
# print(type(s1))

# =======================

# Set Function 

# 1 : len  : Returns the number of items in the list.
 
# 2 : min  : Returns the smallest item in the list. 

# 3 : max  : Returns the largest item in the list.

# 4 : sum  : Returns the sum of all numeric items in the list.



# Set Method 

# s1 = set()

# 1  : add : Adds a single element to the set.

# 2  : pop : Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty. 

# 3  : remove : Removes a specified element from the set. Raises a KeyError if the element is not found.

# 4  : clear : Removes all elements from the set, making it empty. 

# 5  : union : Returns a new set containing all unique elements from both sets.

# 6  : update : Adds all elements from an iterable (like another set, list, or tuple) to the current set.

# 7  : intersection : Returns a new set containing only the common elements between the sets.

# 8  : intersection_update : Updates the calling set with the intersection of itself and another set.

# 9  : difference : Returns a new set containing elements present in the first set but not in the second.

# 10 : difference_update : Updates the calling set by removing elements present in another set.


# 1  : add : 

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s1.add(14)
# s1.add(11)
# print(s1)

# 2  : pop :

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s1.pop()
# print(s1)


# 3  : remove :

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s1.remove(3)
# print(s1)


# 4  : clear :

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s1.clear()
# print(s1)

# 5  : union :

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s2 = {11,12,13,14,15}
# print(s1.union(s2))


# 6  : update :

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s2 = {11,12,13,14,15}
# s1.update(s2)
# print(s1)

# 7  : intersection :

# s1={1,2,3,4,5,6,7,8,9,10}
# s2={11,12,13,14,15,16,17,18,19,20,1}
# s3=s1.intersection(s2)
# print(s3)


# 8  : intersection_update :

# s1={1,2,3,4,5,6,7,8,9,10}
# s2={11,12,13,14,15,16,17,18,19,20,1}
# s1.intersection_update(s2)
# print(s1)

# 9  : difference :

# s1={1,2,3,4,5,6,7,8,9,10}
# s2={11,12,13,14,15,16,17,18,19,20,1}
# s3=s1.difference(s2)
# print(s3)

# 10 : difference_update 
# s1={1,2,3,4,5,6,7,8,9,10}
# s2={11,12,13,14,15,16,17,18,19,20,1}
# s1.difference_update(s2)
# print(s1)

# =========================

# Task 1 : 

# t1 = (1,2,3,4,5,6,7,8,9,10)

# t2=t1+ tuple(range(11,16))
# print(t2)
    

# output : (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)


# Task 2 : 

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s2 = {11,12,13,14,15}

# for i in s2:
#    s1.add(i)
# print(s1)
# output  : {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# using add method


# Task : 3

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s2 = {11,12,13,14,15,5,6,7}

# print(s1 & s2)


# output : {5,6,7} 
# no use intersection method 