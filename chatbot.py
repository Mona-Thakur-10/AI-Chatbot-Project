responses = {"how are you":"I am Fine!",
             "hy":"hie there!",
             "hello":"hie there!",
             "help":"How can I help?",
             "bye":"Good Bye!",
             "thanks":"Wlecome!"
            }
while True:
    user = input("You: ").lower().strip()
    if user == "exit":
        print("Bot: Bye!")
        break
    
    reply = responses.get(user,"I dont Understand..")
    print("Bot: ", reply) 