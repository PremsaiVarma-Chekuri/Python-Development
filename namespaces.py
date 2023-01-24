x = "GLobal variable"
def foo_bar():
    print(9)

def foo():
    foo_bar()
    print(x)
#print(x)
foo()
print(x)