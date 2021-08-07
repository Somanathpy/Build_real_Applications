def concatenate(*args):
    result = ''
    for arg in args:
        result +=" "+ arg
    return result

print(concatenate("Hello", "How", "you"))

def concatenate1(**kwargs):
    result=""
    for arg in kwargs.values():
        result += " "+arg
    return result

print(concatenate1(a="Python", b="is" , c="great"))

'''def concatenate1(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate1(a="Real", b="Python", c="Is", d="Great", e="!"))'''


def find_winner(**kwargs):
    return max(kwargs,key=kwargs.get)

print(find_winner(Andy=15,Sam=17,robert=256,jiljil=567))