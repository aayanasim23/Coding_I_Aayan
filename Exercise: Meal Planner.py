meal = input("What meal are you looking for? (breakfast, lunch, dinner, thanksgiving, halloween, barbeque)")

if meal == "breakfast":
    print("How about some avocado on toast?")
    print("What about some cereal?")
elif meal == "lunch":
    print("Mcdonalds?")
    print("How about burger king?")
elif meal == "dinner":
    print("Chicken over rice?")
    print("How about fast food?")
elif meal == "thanksgiving":
    print("TURKEY!?")
    print("More Turkey?")
elif meal == "halloween":
    print("Pumpkin pie?")
    print("How about nothing?")
elif meal == "barbeque":
    print("Grilled Burgers")
    print("Grilled hot dogs?")
else:
    print("Please enter a meal option: breakfast, lunch, dinner, thanksgiving, halloween, or barbeque.")
