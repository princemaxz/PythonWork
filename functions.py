def hello_money():
    print("Hello World")


hello_money()

# functions that takes or receive parimeters


# def sum(num1, num2):
#     print(num1 + num2)


# sum(1, 4)
# sum(15, 4)
# sum(1001, 4)


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2


total = sum()
print(total)


# for passing multiple parameters


def multiple_choice(*args):
    print(args)
    print(type(args))


multiple_choice("joe", "prince", "modzaka")


def multi_task_item(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_task_item(first="prince", last="modzaka")
