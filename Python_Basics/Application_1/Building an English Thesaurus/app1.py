import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):
    word = word.lower()
    #word_title = word.title()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif  len(get_close_matches(word,data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y  if yes, or press N if no." % get_close_matches(word,data.keys())[0])
        if yn == "y" :
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "n" :
            return "The word does't exist, plesae double check it"
        else:
            return " we didn't understand your entry"

        #data[get_close_matches(word,data.keys())[0]]
    else:
        return " The word doesn't exist , please double check it"


word = input("enter a word to find its definition: ")
output = definition(word)
#print(type(output))

if type(output) == list :
    for item in output:
        print(item)
else:
    print(output)