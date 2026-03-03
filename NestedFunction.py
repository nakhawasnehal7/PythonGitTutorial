def outer():
    def Inner():
        print('Inner function')

    print('outer')

    return Inner


f = outer()
f()
