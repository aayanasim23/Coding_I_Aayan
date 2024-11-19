print("My name is HAL-9, I am your personal Chatbot.")

name = input("What's your name?")

print("Nice to meet you, " + name)


while True:
    
    user_command = input("Tell me to do something," + name + ": ")

    if user_command == "Print your name":
        print("HAL-9")
        break
    else:
        print("I’m sorry " + name + ", I’m afraid I can’t do that.")