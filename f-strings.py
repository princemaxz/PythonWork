# THE OLD WAY OF DOING IT

person = "prince"

coins = 3

print("\n" + person + " has " + str(coins) + " coin left.")

# Another way of doing the above is to use %s
message = "\n%s has %s coin left." % (person, coins)

print(message)

# Another way of doing it is to use {}

message = "\n{} has {} coin left.".format(person, coins)

print(message)


message = "\n{1} has {0} coin left.".format(coins, person)

print(message)


message = "\n{person} has {coin} coin left.".format(coin=coins, person=person)

print(message)


player = {"person": "prince", "coins": 3}

message = "\n{person} has {coins} coin left.".format(**player)

print(message)


# F-STRINGS! THIS IS THEWAY

message = f"\n{person} has {coins} coin left."
print(message)

message = f"\n{person} has {3*4} coin left."
print(message)

message = f"\n{person.upper()} has {3*4} coin left."
print(message)

message = f"\n{player['person']} has {3*4} coin left."
print(message)


# YOU CAN PASS FORMATTING OPTIONS

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 12):
    print(f"2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 12):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
