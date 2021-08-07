temps = [ 221, 234, 340, 230]

'''
regular for loops for list

new_temps = []

for temp in temps:
    new_temps.append(temp/10)

print(new_temps)'''


'''List Comprehensions
'''
new_temps = [ temp/10 for temp in temps]
print(new_temps)

