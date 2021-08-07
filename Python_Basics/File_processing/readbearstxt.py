'''file = open("bears.txt")
content = file.read()
file.close()

print(content)'''


''' if we use open() method, file object will be in RAM, hence we have to close the file object once we done the processing
using file.close() method. using "with" is better option to open the file because "with" method close the file 
object implicitly
'''
with open("bears.txt") as file:
    content = file.read()

print(content)
