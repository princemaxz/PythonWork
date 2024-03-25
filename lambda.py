square = lambda num: num * num

print(square(4))

onetwo = lambda num: num + 3

print(onetwo(4))


sum_total = lambda a, b: a + b

print(sum_total(10, 4))

#######################################


def funcbuilder(x):

    return lambda num: num + x


addten = funcbuilder(10)
addtwenty = funcbuilder(20)

print(addten(7))
print(addtwenty(7))


############################################


numbers = [2, 4, 15, 65, 23, 63, 10, 7]
square_nums = map(lambda num: num * num, numbers)
print(list(square_nums))


######################################### from chatGPT
# Define a list of numbers
numbers1 = [1, 2, 3, 4, 5]

# Use map() function with lambda to square each number in the list
squared_numbers = list(map(lambda x: x**2, numbers1))

# Print the squared numbers
print("Original numbers:", numbers1)
print("Squared numbers:", squared_numbers)

##############################################################


odd_num = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_num))


##########################################################
from functools import reduce


number = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, number, 10)

print(total)

print(sum(number, 10))


############################################################

names = ["jojo", "kudzo", "prince", "kwame nana-arko modzaka", "noagbe"]

chat_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(chat_count)
