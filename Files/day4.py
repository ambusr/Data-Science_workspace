# ==================================================
# PYTHON SET – CREATION, ACCESSING, METHODS, FUNCTIONS

# ==================================================

# 1. SET CREATION
# --------------------------------------------------
# Set is an unordered collection of unique elements

# s1 = {1, 2,8, 5,6,4}
# s2 = {"apple", "banana", "cherry"}
# s3 = {1, "python", 3.5, True}

# print(s1)
# print(s2)
# print(s3)
# print(type(s1))

# s=[1,2,2,3,5,7,4,9,2]
# p=set(s)
# f=list(p)
# print(f)

# print("\n-----------------------------\n")

# # # EMPTY SET (IMPORTANT)
# s = set()
# print(s)
# print(type(s))

# print("\n-----------------------------\n")

# # 2. ADD ELEMENTS TO SET
# # --------------------------------------------------
# s = {1, 2, 3}
# s.add(4)
# print(s)

# s.update([5, 6, 7])
# print(s)

# # print("\n-----------------------------\n")

# # # 3. REMOVE ELEMENTS FROM SET
# # # --------------------------------------------------
# s={3, 4, 5, 6, 7}
# remove()
# s.remove(9)
# print(s)

# # discard() – no error if element not present
# s.discard(10)
# print(s)

# pop() – removes random element
# s.pop()
# print(s)

# print("\n-----------------------------\n")

# # 4. SET OPERATIONS
# # --------------------------------------------------
# a = {'a','d','b'}
# b = {'b','c'}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))

# print("\n-----------------------------\n")

# # 5. SET METHODS
# # --------------------------------------------------
# s = {1, 2, 3}

# print(s.copy())

# s.clear()
# print(s)

# print("\n-----------------------------\n")

# # 6. SET FUNCTIONS
# # --------------------------------------------------
# s = {5, 2, 8, 1, 3}

# print(len(s))
# print(max(s))
# print(min(s))
# print(sum(s))
# print(sorted(s,reverse=True))


# # 8. MEMBERSHIP CHECK
# # --------------------------------------------------
# s = {10, 20, 30}

# print(20 in s)
# print(50 not in s)

# print("\n--- END OF SET TOPICS ---")


# # ==================================================
# # PYTHON DICTIONARY – CREATION, ACCESSING, METHODS

# # ==================================================

# # 1. DICTIONARY CREATION
# # --------------------------------------------------
# # Dictionary stores data as key : value pairs

# d1 = {
#     "name": "Sona","age": 22,"course": "Python"
# }

# print(d1)
# print(type(d1))

# print("\n-----------------------------\n")

# # EMPTY DICTIONARY
# d = {}
# print(d)

# print("\n-----------------------------\n")

# # 2. ACCESSING DICTIONARY VALUES
# # --------------------------------------------------
d1 = {
    "name": "Sona","age": 22,"course": "Python"
}

# print(d1["course"])
# print(d1.get("age"))

# print("\n-----------------------------\n")

# # 3. MODIFY & ADD ELEMENTS
# # --------------------------------------------------
# d1["age"] = 23
# d1["city"] = "Chennai"
# print(d1)

# print("\n-----------------------------\n")

# # 4. REMOVE ELEMENTS
# # --------------------------------------------------

# # pop()
# d1.pop("course")
# print(d1)

# popitem()
# d1.popitem()
# print(d1)

# print("\n-----------------------------\n")

# # 5. DICTIONARY METHODS
# # --------------------------------------------------
# d = {"a": 1, "b": 2, "c": 3}

# print(d.keys())
# print(d.values())
# print(d.items())

# print("\n-----------------------------\n")

# # update()
# d.update({"d": 4, "e": 5})
# print(d)

# # copy()
# p = d.copy()
# print(p)

# # clear()
# d.clear()
# print(d)

# print("\n-----------------------------\n")


# student = {"name": "Sona", "age": 22, "course": "Python"}

# # 7. CHECK KEY IN DICTIONARY
# # --------------------------------------------------
# print("name" in student)
# print("marks" not in student)

# print("\n-----------------------------\n")

# # 8. DICTIONARY FUNCTIONS
# # --------------------------------------------------
# print(len(student))

# print("\n-----------------------------\n")

# # 9. NESTED DICTIONARY
# # --------------------------------------------------
# students = {
#     1: {"name": "Sona", "age": 22},
#     2: {"name": "Anu", "age": 21}
# }

# print(students)
# print(students[2]["name"])

# print("\n--- END OF DICTIONARY TOPICS ---")
