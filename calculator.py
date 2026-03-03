import time

def add(num1,num2):
    # pass
    return num1 + num2

def subtract(num1,num2):
    # pass
    return num1 - num2

def multiply(num1,num2):
    # pass
    return num1 * num2

def divide(num1,num2):
    # pass
    return num1 / num2

def root(num1,num2):
    pass

def exponentiate(num1,num2):
    # pass
    time.sleep(5)
    i = 1
    base = num1

    while i < num2:
        num1 *= base
        i += 1

    return num1

