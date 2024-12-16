print("My name is GPT Junior, I am your personal Chatbot.")

name = input("What's your name? ")

print("Nice to meet you, " + name + "! Ask me: How are you?, What's your favorite color?, Tell me a joke, What's your favorite food?, Do you like to travel?")

conversation_options = ["How are you?", "What's your favorite color?", "Tell me a joke.", "What's your favorite food?", "Do you like to travel?"]

while True:
    user_input = input("Your response: ")

    if user_input in conversation_options:
        if user_input == "How are you?":
            print("I'm doing well, thank you!")
        elif user_input == "What's your favorite color?":
            print("My favorite color is blue.")
        elif user_input == "Tell me a joke.":
            print("Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!")
        elif user_input == "What's your favorite food?":
            print("I don't eat, I'm a chatbot!")
        elif user_input == "Do you like to travel?":
            print("I would love to travel, but unfortunately, I'm stuck in this computer. Where would you like to travel?")
            for i in range(1):
                travel_input = input("Your travel destination: ")
                print("That sounds like a great place to visit!")
                print("Where else would you like to travel?")
                travel_input2 = input("Your travel destination: ")
                print("That sounds like a great place to visit!")
                travel_input3 = input("What would you like to eat there?")
                print("That sounds delicious!")

        else:
            print("Sorry, I didn't understand that. Let's try again.")
    else:
        break

print("It was nice chatting with you!")
