phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has phone number {}".format(pair[0],pair[1]))


for key,value in phone_numbers.items():
    print("{} has phone number {}".format(key,value))


for key,value in phone_numbers.items():
    print("{} has phone number {}".format(key,value))


for key,value in phone_numbers.items():
    print("%s: %s" %(key,value))


for key,value in phone_numbers.items():
    value = value.replace('+','00')
    print("%s: %s" %(key,value))