def sentence_maker(phrase):
    interrogatives = ("how","what","why","where")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

#print(sentence_maker("how are you doing"))

total_message = ''
while True:

    user_input = input("Say Something: ")
    if user_input == '\end':
        break
    else:
        total_message += sentence_maker(user_input)

print(total_message)
