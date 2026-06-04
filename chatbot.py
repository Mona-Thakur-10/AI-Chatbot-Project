print("AI Chatbot Started!")
responses = {"how are you":"I am Fine!",
             "hy":"hie there!",
             "hello":"hie there!",
             "good morning":"Good Morning!",
             "good evening":"Good Evening!",
             "help":"How can I help ?",
             "bye":"Good Bye!",
             "thanks":"Wlecome!"
            }

while True:
    user = input("You: ").lower().strip()
    if user == "exit":
        print("Bot: Bye!")
        break
    
    reply = responses.get(user,"Sorry,I dont Understand that.. \nPlease try another Question.")
    print("Bot: ", reply) 
