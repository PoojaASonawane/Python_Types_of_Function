#immutable

def add(x,y):
    print(id(x))
    print(id(y))
a=100
b=200
print(id(a))
print(id(b))
add(a,b)

#mutable

def show(mylist):
    print(id(mylist))
    mylist.append(78)
    print(mylist)
list1=[1,2,3]
print(id(list1))
show(list1)
