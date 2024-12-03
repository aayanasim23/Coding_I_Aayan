def idk():
    try:
        numb_1 = int(input("Give me a number"))
        numb_2 = int(input("Give me another number"))
        print("You inputted,", numb_1, numb_2)
    except:
        TypeError
        print("Give me a integer instead!")

idk()