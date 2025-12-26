

# l1 = [1,2,"python",True,None,False,"django",-1]
# print(l1)
# print(type(l1))


# indexing and slicing 

# l1 = [1,2,"python",True,None,False,"django",-1]

# print(l1[0])
# print(l1[1])
# print(l1[3])
# print(l1[-2])

# print(l1[0:3])
# print(l1[0:])
# print(l1[:5])
# print(l1[:])

# print(l1[0:5:2])


# list function 

# 1 : len  : Returns the number of items in the list.
 
# 2 : min  : Returns the smallest item in the list. 

# 3 : max  : Returns the largest item in the list.

# 4 : sum  : Returns the sum of all numeric items in the list.

# 1 : len  :

# l1 = [1,2,"python",True,None,False,"django",-1]
# print(len(l1))

# 2 : min  :

# l1 = [1,2,5,6,8,9,3,2,1,0,32,1,1]
# print(min(l1))


# 3 : max  :


# l1 = [1,2,5,6,8,9,3,2,1,0,32,1,1]
# print(max(l1))


# 4 : sum  :

# l1 = [1,2,5,6,8,9,3,2,1,0,32,1,1]
# print(sum(l1))


# list method 

# 1 : append :  Adds a single element to the end of the list.

# 2 : extend :  Adds all elements from an iterable (like another list, tuple, or string) to the end of the current list.

# 3 : insert :  Inserts an element at the specified index.

# 4 : pop : Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element.
  
# 5 : remove : Removes the first occurrence of the specified value from the list.

# 6 : clear :  Removes all elements from the list, making it empty.

# 7 : del : The del keyword in Python is used to delete entire lists or slices.

# 8 : count : Returns the number of times a specified value appears in the list. 

# 9 : index : Returns the index of the first occurrence of the specified value. Optional start and end arguments can limit the search range. 

# 10 : sort : Sorts the elements of the list in-place. By default, it sorts in ascending order. key can be used for custom sorting, and reverse=True sorts in descending order.

# 11 : reverse : Reverses the order of the elements in the list in-place. 




# 1 : append :

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l1.append(11)
# print(l1)


# 2 : extend :

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l1.extend([11,2])
# print(l1)

# 3 : insert :

# l1 = [1,2,3,4,5,6,8,9,10]
# l1.insert(6,7)
# print(l1)


# 4 : pop :

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l1.pop()
# print(l1)

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l1.pop(2)
# print(l1)

# 5 : remove : 

# l1 = [1,2,3,4,5,6,7,8,9,10,6,7]
# l1.remove(7)
# print(l1)


# 6 : clear :


# l1 = [1,2,3,4,5,6,7,8,9,10,6,7]
# l1.clear()
# print(l1)

# 7 : del :


# l1 = [1,2,3,4,5,6,7,8,9,10,6,7]
# print(l1)
# del l1
# print(l1)

# 8 : count :


# l1 = [1,2,3,4,5,6,7,8,9,10,6,7]
# print(l1.count(7))


# 9 : index :


# l1 = [1,2,3,4,5,6,7,8,9,10,6,7]
# print(l1.index(7))



# 10 : sort :

# l1=[5,4,2,6,7,8,5,4,33,2,22,2,3,3,4,678,7,65432]
# l1.sort()
# print(l1)

# l1=[5,4,2,6,7,8,5,4,33,2,22,2,3,3,4,678,7,65432]
# l1.sort(reverse=True)
# print(l1)


# 11 : reverse :

# l1=[5,4,2,6,7,8,5,4,33,2,22,2,3,3,4,678,7,65432]
# l1.reverse()
# print(l1)


# =====================

# l1 = [1,3,"Python",True,None,False,"django",-6,-10]
# for i in l1:
#     print(i)



# l1 = [1,3,"Python",True,None,False,"django",-6,-10]
# for i in range(len(l1)):
#     print(i,l1[i])


# ========================

# Task : 1 

# l1=[1,2,3,54,3,2,2,4,56,7,8,9,5,43,4]

# number=0
# for i in l1:
#     number+=i
# print(number)
      

# output : all value find sum (no use sum function)



# Task : 2 

# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[11,12,13,14,15]

# for i in l2:
#    l1.append(i)
# print(l1)

# output : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] (no use extend)

# Task : 3

# l1 = 





