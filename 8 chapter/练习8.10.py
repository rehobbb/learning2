def send_message(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"sending message: {current_message}")
        sent_messages.append(current_message)
messages = ['nihao','hello','hi','morning']
sent_messages = []
send_message(messages, sent_messages)
print('\nthe following messages have been sent:')
for sent_message in sent_messages:
    print(sent_message)