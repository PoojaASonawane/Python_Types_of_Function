#global
x=123
def show():
    x=100
    def disp():
        nonlocal x
        x=300
        print(x)
    disp()
    print(x)
show()
print(x)