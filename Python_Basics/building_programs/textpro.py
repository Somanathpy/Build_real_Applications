
'''total_message = ''

while True:
    message = input("Say Something:")
    if message == '\end':
        break
    elif "who" in message or "why" in message or "how" in message or "what" in message:
        message = ' ' + message.title() + "?"
    else:
        message =  ' ' + message.title() + "."
    total_message += message

print(total_message)   '''




