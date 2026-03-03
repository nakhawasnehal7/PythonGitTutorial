def welcome():
    print('Welcome Function')


def fun(f):
    f()


fun(welcome)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def arithmatic(f, x, y):
    return f(x, y), " ss"


print(arithmatic(add, 7, 9))
print(arithmatic(sub, 7, 9))


def add(feet, inches=10):
    return inches + feet


print(add(5))
print(add(5, 5))
print(add(inches=5, feet=5))
print(add(feet=5, inches=5))
print(add(5, feet=5))
