monday_weathers = [ 10.45, 12.56, 13.67, 17.89]

for temp in monday_weathers:
    print(round(temp))


for letter in 'Hello':
    print(letter.upper())


def celcius_to_kelvin(cels):
    return cels + 273.15

for temp in monday_weathers:
    print(celcius_to_kelvin(temp))