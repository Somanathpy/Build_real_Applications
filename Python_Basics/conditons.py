def mean(value):
    if type(value) == dict:
         the_mean = sum(value.values()) / len(value.values())
    else:
        type(value) == tuple or type(value) == list or type(value) == set
        the_mean = sum(value) / len(value)
        
    return the_mean

print(mean({'jack': 10,'Lolo': 15, 'Lily': 56}))
print(mean((1,2,3)))
print(mean([1,2,3]))
print(mean((2,4,6))) 
    
         
       