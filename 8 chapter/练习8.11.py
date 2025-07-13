def send_message(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"sending message: {current_message}")
        sent_messages.append(current_message)
def print_messages(messages):
    for message in messages:
        print(message)
    print('\n')
messages = ['nihao','hello','hi','morning']
sent_messages = []
send_message(messages[:], sent_messages)
print('\nthe following messages have been sent:')
print_messages(sent_messages)
print_messages(messages)