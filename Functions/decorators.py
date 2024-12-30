#decorators
def decor(func):
    def wrapper():
        print("******")
        func()
        print("******")
    return wrapper

def fun():
    print("inside")

fun1 = decor(fun)

fun1()


