# DICTONARY
# Creating a dictionary, checking type and lengh
Band = {"Vocals": "plant", "guiter": "page"}

BAnd2 = dict(Vocals="plant", guitar="page")

print(Band)
print(BAnd2)
print(type(BAnd2))
print(len(BAnd2))

# How to access Item from dictionary
print(Band["Vocals"])
print(Band.get("guiter"))

# Listing all keys in dictionary
print(Band.keys())

# Listing all values in dictionary
print(Band.values())

# Listing of keys/value pairs as tuples in dictionary
print(Band.items())

# Verify if key exist
print("guiter" in Band)
print("drum" in Band)

# Change Values
Band["Vocals"] = "caverdel"
Band.update({"bass": "jpj"})
print(Band)

# Remove item
print(Band.pop("bass"))
print(Band)

Band["drum"] = "boharm"
print(Band)

print(Band.popitem())  # This willreturn tuples
print(Band)

# Delete and clear
Band["drum"] = "boharm"

del Band["drum"]

BAnd2.clear()
print(BAnd2)

BAnd2.clear

del BAnd2

# Copy dictionary

# BAnd2 = Band  # this creat reference
# print("Bad Copy!")
# print(BAnd2)
# print(Band)

# BAnd2["drums"] = "Prince"
# print(Band)

BAnd2 = Band.copy()
BAnd2["drums"] = "Prince"
print("Good Copy!")
print(Band)
print(BAnd2)

# or use dict() constructor function to copy
band3 = dict(Band)
print("Good Copy!")
print(band3)


# Nested Dictionary

member1 = {"Name": "plant", "Instrument": "Vocals"}
member2 = {"Name": "page", "Instrument": "guiter"}

Band = {"member1": member1, "member2": member2}
print(Band)

print(Band["member1"]["Name"])

# Set in dictionary
nums = {1, 2, 3, 4, 5}
nums2 = set((1, 2, 3, 4, 5))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))


# No duplicate allowed

nums = {1, 2, 2, 2, 3, 4}
print(nums)

# True is a dupe of 1, and False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# To check is a value is in a set

print(2 in nums)

# But you cannot refer to an element in the set with an index position or key

# Add new element to a set
nums.add(8)
print(nums)

# Add Element from one setto another
morenums = {7, 6, 10, 11}
nums.update(morenums)
print(nums)

# you can use update with list, tuple and dictionary too

# Merge two set to creat new set

one = {1, 2, 3}
two = {4, 6, 8}

mynewset = one.union(two)
print(mynewset)

# Keeping only the duplicate
one = {1, 2, 3, 6, 4}
two = {4, 6, 2, 3, 8}

one.intersection_update(two)
print(one)

# Keeping everything except the duplicate
one = {1, 2, 3, 6, 4}
two = {4, 6, 2, 3, 8}

one.symmetric_difference_update(two)
print(one)
