# Loop with break
# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# WHILE LOOP
# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# FOR LOOP

names = ["prince", "joe", "maxz"]
# for x in names:
#     print(x)

# for j in "mississippi":
#     print(j)

# for x in names:
#     if x == "joe":
#         break
#     print(x)

# for x in names:
#     if x == "joe":
#         continue
#     print(x)

# for x in range(4):
#     print(x)
for x in range(0, 100, 5):
    print(x)
else:
    print("Glade that's over!")

# names = ["prince", "joe", "maxz"]
# actions = ["james", "code", "five"]
# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")


names = ["prince", "joe", "maxz"]
actions = ["james", "code", "five"]
for action in actions:
    for name in names:
        print(name + " " + action + ".")
