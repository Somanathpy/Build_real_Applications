def mean(*args):
    return sum(args) / len(args)


print(mean(1,2,3,4,5))

def foo(*args):
    args = [str.upper() for str in args]
    return sorted(args)

print(foo("lily","jack","Lolo"))