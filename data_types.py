# String data type

# literal assignment

first = "Prince"
last = "Modzaka"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# # Concatination
# full_name = first + " " + last
# print(full_name)
# full_name += "!"
# print(full_name)
# full_name -= "!"
# print(full_name)

# Casting a number to a string

decade = str(1982)
print(type(decade))
print(decade)

statement = "I like reggae from the " + decade + "s."
print(statement)

# Multiple line
multipleline = """
hey, how are you?                                

I was just checking in      

                            All good?


"""
print(multipleline)

# escaping special character

# sentence = "I'm back at work!\tHey!\n\nwhere's this at\\location?"
# print(sentence)


# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

print(multipleline.title())
print(multipleline.replace("good", "ok"))
print(multipleline)

# Thisisto check the lenth and add more white space
print(len(multipleline))

multipleline += "                                               "
multipleline = "                    " + multipleline
print(len(multipleline))

# This is toremove whitespace from left and right and count the lenght as well

print(len(multipleline.strip()))
print(len(multipleline.lstrip()))
print(len(multipleline.rstrip()))

print("")

# Build menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Tea".ljust(16, ".") + "$3".rjust(4))
print("Koko".ljust(16, ".") + "$5".rjust(4))

print(" ")

# String value index

print(first[1])
print(first[-1])
print(first[0])
print(first[2])
print(first[1:-1])
print(first[1:])

# Some methods return boolen data

print(first.startswith("P"))
print(first.endswith("Z"))

# Boolen data type

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Integer type

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type

gpa = 4.01
y = float(3.89)
print(type(gpa))

# complex type

com_value = 5 + 4j
print(type(com_value))
print(com_value.real)
print(com_value.imag)

# Build-in function for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string toa number

zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# error if you attempt tocast incorrect data
zip_value = int("new york")
