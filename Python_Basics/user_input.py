def temp_check(temp):
    if temp > 7:
        return "Hot"
    elif temp == 7:
        return "warm"
    else:
       return "Cold"

user_input = float(input("enter Temperature: "))
print(temp_check(user_input))
