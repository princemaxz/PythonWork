user = ["Prince", "john", "Kudzo"]

data = ["Prince", 42, True]

emptylist = []

print("Prince" in user)
print(42 in data)
print("kofi" in user)

print(user[0])
print(user[-1])
print(user[1])

# This look for position of the data
print(user.index("Kudzo"))

# This is to get a range of value

print(user[0:2])
print(user[1:])
print(user[0:])
print(user[-3:-1])

# This is to show the lenght of our data

print(len(user))

# This is to add a data to a existing list
user.append("Maxz")
print(user)

# This is to add a list to a existing list
user += ["Keli"]
print(user)

user.extend(["Modzaka", "Mael", "Jojo"])
print(user)

# This is to pass in pre-exhisting list
# user.extend(data)
# print(user)

# This is to insect a data to a specific position
user.insert(0, "Majesty")
print(user)

# This is to insect 2/more data to a position existing list
# (2:2 means start and end at same postion hence no replacement)
user[2:2] = ["Theresa", "Dzidzor"]
print(user)

# To replace value
# (1:3 means start from 1 and end at 2. this is also called SLICE)
user[1:3] = ["Sam", "Noagbe"]
print(user)

# How to remove data from a list
user.remove("Majesty")
print(user)

# Using pop method which remove last data n place it outside
print(user.pop())
print(user)

# This isto Delete data
del user[0]
print(user)

# To delete a list
# del data
# print(data)
data.clear()
print(data)

# This is to sort data in alphabetical order including lower keys
user[1:2] = ["adzo"]
user.sort(key=str.lower)
print(user)

# This is to reverse numbers
num = [2, 45, 34, 2, 7, 4, 0]
num.reverse()
print(num)

# This is to reverse numbers(ascending and decending)
# num.sort(reverse=True)
# print(num)
# num.sort(reverse=False)
# print(num)

# This is to sort a list without modifying it (global sorting)
print(sorted(num, reverse=True))
print(num)

# To make a copy of list b4 sorting.( 3 ways)
mynumcopy = num.copy()
numcopy = num[:]
mycopy = list(num)

print(mynumcopy)
print(numcopy)
mycopy.sort()
print(mycopy)
print(num)

# check the type
print(type(num))

# Another way of creating a list
mylist = list([1, 4, "Prince", True])
print(mylist)


# TUPLES (tuples cannot be changed)
mytuples = tuple((1, 8, "Maxz2", False))
anothertuple = (4, 6, 8, 4, 6, 4)

print(mytuples)
print(type(anothertuple))
print(type(mytuples))

# Unpacking tuple

newlist = list(mytuples)
newlist.append("Man")
newtuple = tuple(newlist)
print(newtuple)

(one, *six, hey) = anothertuple
print(one)
print(six)
print(hey)

# Count the number of items using tuple
print(anothertuple.count(4))
