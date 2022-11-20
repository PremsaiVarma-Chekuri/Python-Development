x = "GLobal variable"

def foo():
    global x
    x = "Local Variable"
    print(x)
print(x)
foo()
print(x)