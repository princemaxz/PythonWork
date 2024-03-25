# GLOBAL SCOPE
Name = "prince"
count = 2


# def greetings():
#     color = "blue" # LOCAL SCOPE
#     print(color)
#     print(Name)


# calling another function inside a fuction(NESTED)
def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greetings(Name):
        nonlocal color
        color = "red"
        print(color)
        print(Name)

    greetings("prince")


another()
