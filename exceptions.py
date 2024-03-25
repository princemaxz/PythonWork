class JustNotCoolError(Exception):
    pass


x = 2

try:
    raise JustNotCoolError("This error is not cool man")
    # raise Exception('I am customar exception')
    # # print(x / 1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means there is something undefine")

except ZeroDivisionError:
    print("please do not divide by zero")

except Exception as error:
    print(error)
else:
    print("there is no error")

finally:
    print("I am going to print with or without an error")
