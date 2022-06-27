def sqr(x):
    y=x*x
    return y
a=sqr(12)
print(a)
###############################
## using lambda fun ###
sqr=lambda x:x*x
print(type(sqr))
a=sqr(12)
print(a)

###############################
add = lambda x,y,z:x+y+z
print(add(10,20,30))

##########     Filter Fun()   ######################

def even(list1):
    temp=[]
    for x in list1:
        if x%2==0:
            temp.append(x)
    return temp
mylist = [1,2,3,4,5,6,7,8,9,10]
list2 = even(mylist)
print(list2)
###########################################
mylist=[1,2,3,4,5,6,7,8,9,10]
fun1=lambda x:x%2==0
list2=list(filter(fun1,mylist))
print(type(list2))
print(list2)
##########################################
mylist=[1,2,3,4,5,6,7,8,9,10]
list2=list(filter(lambda x:x%2==0,mylist))
print(list2)

#########    map fun()    ################
def sqr(list1):
    temp=[]
    for x in list1:
        temp.append(x*x)
    return temp
mylist=[1,2,3,4,5,6,7,8,9,10]
list2=sqr(mylist)
print(list2)
#########################################
mylist=[1,2,3,4,5,6,7,8,9,10]
list2=list(map(lambda x:x*x, mylist))
print(list2)

###########################################
s1=input("Enter values")
arr=s1.split(",")
print(arr)
#########################################
list2=list(map(int,arr))
print(list2)
############################################
list2=list(map(int,input("Enter values").split(',')))
print(list2)


