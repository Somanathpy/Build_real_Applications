string = input("enter a string:")

#if string.find("who") or string.find("why") or string.find("How") or string.find("what"):
    #print(string + "?")
#else:
   #break



if "who" in string or "why" in string or "how" in string or "what" in string:
    print(string + " ? ")
else:
    print(string)