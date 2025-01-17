def enthusiasm(enthusiasm):
    if enthusiasm.isupper():
        print("You are already enthusiastic!")
    else:
        enthusiasm2 = enthusiasm.upper() + "!"
        return enthusiasm2

enthusiasm("hi")