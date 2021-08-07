list1 = [ 99, 100, 78, 45, "no data", 567.67, 456.56, "Lily"]

'''def foo(list):
    return [ i for i in list1 if isinstance(i,float)]

print(foo(list1))'''

def foo1(lst):
    return [ i if isinstance(i,int)  else  0 for i in lst]

print(foo1(list1))