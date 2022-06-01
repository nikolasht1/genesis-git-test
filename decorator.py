def deco(func):
    def inner():
        print("It's decorator")
        func()
     return inner

@deco
def target():
    print("It's target()")

target()

