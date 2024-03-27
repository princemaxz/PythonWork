import os

# r = read
# a = append
# w = write
# x = create

# Read-Error if it doesnt exist

f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("name_list.txt")
    print(f.read())

except:
    print("The file you want to read doesnt exist")

finally:
    f.close()

# Append Create the file if it doesnt exist

f = open("names.txt", "a")
f.write("nail\n")
f.close()


f = open("names.txt")
print(f.read())
f.close()


# Write (overwrite)

f = open("context.txt", "w")
f.write("I deleted all ofthe context")
f.close()

f = open("context.txt")
print(f.read())
f.close()


# two ways of creating a new file

# Open a file for writing, create a file if it does not exist

f = open("name_list", "w")
f.close()

# Creates a specified file but return an error ifthe file does not exist

if not os.path.exists("prince.txt"):
    f = open("prince.txt", "x")
    f.close()

# Delete a file

# Avoid Error if it doesnt exist

if os.path.exists("prince.txt"):
    os.remove("prince.txt")
    print("the file you want to delete does not exist")


with open("more_name.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
