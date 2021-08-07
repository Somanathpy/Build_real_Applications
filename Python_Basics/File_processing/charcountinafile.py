def foo(chararcter, filepath="bears.txt"):
    file = open(filepath)
    content = file.read()
    return(content.count(chararcter))

print(foo('American'))