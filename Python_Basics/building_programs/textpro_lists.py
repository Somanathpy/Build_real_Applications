def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("why","how","where","what")
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    

sentence = []

while True:
    user_input = input("Say Something: ")
    if user_input == '\end':
        break
    else:
        sentence.append(sentence_maker(user_input))

    
print(' '.join(sentence)) 