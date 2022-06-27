#global
x=123
print(id(x))
def show():
    global x
    x=100
    print(id(x))
    print("local",x)
show()
print("global",x)