def parent_fuction(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + "coins left.")

        elif coins == 1:
            print("\n" + person + " has " + str(coins) + "coin left.")
        else:
            print("\n" + person + " is out of coins")

    return play_game


tommy = parent_fuction("tommy", 6)
eyram = parent_fuction("eyram", 5)

tommy()
tommy()
tommy()

eyram()
