x=10
def func1():
    global x
    print(x)
print("Hi")
func1()

def func2():
    x=5
    print(x)
print(x)
func2()

def outer():
    x="local"

    def inner():
        nonlocal x
        x='nonlocal'
        print("inner ",x)
    inner()
    print("Outer : ", x)
outer()