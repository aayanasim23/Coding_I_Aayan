print("My name is HAL-9, I am your personal Chatbot.")

name = input("What's your name? ")

print("Nice to meet you, " + name)

print("Let's create a story about your Winter Break!")

activity1 = input("Did you go skiing or stay at home during your Winter Break? (Enter 'skiing' or 'home'): ")
if activity1 == "skiing":
    activity2 = input("Did you visit family or travel to a new place? (Enter 'family' or 'travel'): ")
    if activity2 == "family":
        activity3 = input("Did you try a new hobby or relax and unwind? (Enter 'hobby' or 'relax'): ")
        if activity3 == "hobby":
            print("During my Winter Break, I went skiing. It was a lot of fun! I also had the opportunity to visit family. It was a great way to spend time with my loved ones. In addition, I had some time to try a new hobby. It was a much-needed break and I feel refreshed now.")
        else:
            print("Invalid input.")
    elif activity2 == "travel":
        activity3 = input("Did you try a new hobby or relax and unwind? (Enter 'hobby' or 'relax'): ")
        if activity3 == "hobby":
            print("During my Winter Break, I went skiing. It was a lot of fun! I also had the opportunity to travel to a new place. It was a great way to explore and have new experiences. In addition, I had some time to try a new hobby. It was a much-needed break and I feel refreshed now.")
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
elif activity1 == "home":
    activity2 = input("Did you visit family or travel to a new place? (Enter 'family' or 'travel'): ")
    if activity2 == "family":
        activity3 = input("Did you try a new hobby or relax and unwind? (Enter 'hobby' or 'relax'): ")
        if activity3 == "hobby":
            print("During my Winter Break, I stayed at home. It was a relaxing time! I also had the opportunity to visit family. It was a great way to spend time with my loved ones. In addition, I had some time to try a new hobby. It was a much-needed break and I feel refreshed now.")
        else:
            print("Invalid input.")
    elif activity2 == "travel":
        activity3 = input("Did you try a new hobby or relax and unwind? (Enter 'hobby' or 'relax'): ")
        if activity3 == "hobby":
            print("During my Winter Break, I stayed at home. It was a relaxing time! I also had the opportunity to travel to a new place. It was a great way to explore and have new experiences. In addition, I had some time to try a new hobby. It was a much-needed break and I feel refreshed now.")
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
else:
    print("Invalid input.")
