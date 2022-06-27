def show(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)
show(id=100, name='abc')