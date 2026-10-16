# # ==================================================
# # PYTHON LIST – CREATION, ACCESSING, METHODS, FUNCTIONS
# # ==================================================

# # 1. LIST CREATION
# # --------------------------------------------------
# # List is an ordered, mutable collection

# l1 = [1, 2, 3, 4, 5]
# l2 = ["apple", "banana", "cherry"]
# l3 = [1, "python", 3.5, True]

# print(l1)
# print(l2)
# print(l3)
# print(type(l1))

# print("\n-----------------------------\n")

# # 2. ACCESSING LIST ELEMENTS
# # --------------------------------------------------
# l = [10, 20, 30, 40, 50]

# print(l[0])      # first element
# print(l[2])      # third element
# print(l[-1])     # last element
# print(l[-2])     # second last element

# print("\n-----------------------------\n")

# # 3. LIST SLICING
# # --------------------------------------------------
# l = [10, 20, 30, 40, 50]
# print(l[1:4])  --1,2,3
# print(l[:3])   ---0,1,2
# print(l[2:])   ---2,3,
# print(l[::-1])   # reverse list

# print("\n-----------------------------\n")

# # 4. MODIFY LIST ELEMENTS
# # --------------------------------------------------
# l = [1, 2, 3, 4, 5]
# l[1] = 20
# l[-1] = 50
# print(l)

# print("\n-----------------------------\n")

# 5. ADD ELEMENTS TO LIST (METHODS)
# --------------------------------------------------

# # append()
# l = [0, 1, 2]
# l.append(4)
# l.append("python")
# print(l)

# insert()   insert(position,value)
# l.insert(-1, "hhgu")
# print(l)

# # extend()   extend(seq)
# l.extend([5, "pythjh"])
# print(l)

# print("\n-----------------------------\n")

# # 6. REMOVE ELEMENTS FROM LIST (METHODS)
# # --------------------------------------------------

# # remove()---remove specified object from the list 
# l=[1,2,3,4,5,6,7,8]

# l.remove(4)
# print(l)

# # # pop()---remove the specified index value of the list if no insted mention remove the last elemet

# l.pop()
# print(l)

# l.pop(-1)
# print(l)

# # # del ---deleting the index value
# del l[-1]
# print(l)

# print("\n-----------------------------\n")

# # 7. SEARCH & COUNT METHODS
# # --------------------------------------------------
# l = [1, 2, 3, 2, 4, 2]

# print(l.count(2))   #count the occurence of specified object
# print(l.index(3))   #return the index value of the specified object


# print("\n-----------------------------\n")

# # 8. SORTING & REVERSING
# # --------------------------------------------------
# l = [1,3,2,4,2,8]

# l.reverse()
# print(l)

# # l.sort()
# # print(l)

# l.sort(reverse=True)
# print(l)



# print("\n-----------------------------\n")

# # 9. COPY & CLEAR
# # --------------------------------------------------
# l = [1, 2, 3]

# p = l.copy()
# print(p)

# l.clear()
# print(l)

# print("\n-----------------------------\n")

# # 10. LIST FUNCTIONS (BUILT-IN)
# # --------------------------------------------------
# l = [1, 4, 7, 2, 9]
# l=['s','saas']

# print(len(l))
# print(max(l))
# print(min(l))
# print(sum(l))

# print(sorted(l))
# print(sorted(l, reverse=True))

# # print("\n-----------------------------\n")

# # # 13. CHECK ELEMENT IN LIST
# # # --------------------------------------------------
# l = [10, 20, 30,0,2]

# print(0 in l)
# print(20 in l)
# print(50 not in l)

# # print("\n--- END OF LIST TOPICS ---")





# # ==================================================
# # PYTHON TUPLE – CREATION, ACCESSING, METHODS, FUNCTIONS
# # File Name: tuple_topics.py
# # ==================================================

# # 1. TUPLE CREATION
# # --------------------------------------------------
# # Tuple is an ordered, immutable collection

# t1 = (1, 2, 3, 4, 5)
# t2 = ("apple", "banana", "cherry")
# t3 = (1, "python", 3.5, True)

# print(t1)
# print(t2)
# print(t3)
# print(type(t1))

# print("\n-----------------------------\n")

# SINGLE ELEMENT TUPLE  
# t4 = (10,)
# print(t4)
# print(type(t4))

# print("\n-----------------------------\n")

# # 2. ACCESSING TUPLE ELEMENTS
# # --------------------------------------------------
# t = (10, 20, 30, 40, 50)

# print(t[0])      # first element
# print(t[2])      # third element
# print(t[-1])     # last element
# print(t[-2])     # second last element

# print("\n-----------------------------\n")

# # 3. TUPLE SLICING
# # --------------------------------------------------
# print(t[1:4])
# print(t[:3])
# print(t[2:])
# print(t[::-1])   # reverse tuple

# print("\n-----------------------------\n")

# # 4. IMMUTABILITY OF TUPLE
# # --------------------------------------------------
# # Tuples cannot be modified
# t[1] = 100  #  Error
# print(t)

# print("Tuple is immutable")

# print("\n-----------------------------\n")

# # 5. TUPLE METHODS
# # --------------------------------------------------

# # count()
# t = (1, 2, 3, 2, 4, 2)
# print(t.count(2))

# # index()
# print(t.index(3))

# print("\n-----------------------------\n")

# # 6. TUPLE FUNCTIONS (BUILT-IN)
# # --------------------------------------------------
# t = (5, 2, 8, 1, 3)

# print(len(t))
# print(max(t))
# print(min(t))
# print(sum(t))

# print(sorted(t))
# print(sorted(t, reverse=True))

# print("\n-----------------------------\n")



# # 8. CHECK ELEMENT IN TUPLE
# # --------------------------------------------------
# t = (10, 20, 30)

# print(20 in t)
# print(50 not in t)

# print("\n-----------------------------\n")

# # 9. TUPLE PACKING AND UNPACKING
# # --------------------------------------------------
# # Packing
# t = (1, 2, 3)

# # Unpacking
# a, b, c = t
# print(a)
# print(b)
# print(c)
# print(t)

# print("\n-----------------------------\n")

# # 10. CONVERTING BETWEEN LIST AND TUPLE
# # --------------------------------------------------
# l = [1, 2, 3]
# t = tuple(l)
# print(t)

# l2 = list(t)
# print(l2)

# print("\n--- END OF TUPLE TOPICS ---")
