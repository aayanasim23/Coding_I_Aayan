# What is the schools building number 45
# How many floors does the school have
# Who was the 44th president?
# 

scoreboard = 0

Q1 = input("What is the school's building number? A) 45 B) 1019 C) 1049 D) 47")

if Q1 == ("A"): 
    scoreboard = scoreboard + 1
    print("That's correct! Your score: " + str(scoreboard)) 
 
else:
    print("That's incorrect")


Q2 = input("How many floors does the school have A) 6 B) 12 not including the penthouse C) 19 D) 4")

if Q2 == ("B"): 
    scoreboard = scoreboard + 1
    print("That's correct! Your score: " + str(scoreboard)) 
 
else:
    print("That's incorrect")


Q3 = input("Who was the 44th president? A) Donald Trump B) Hunter Biden) C) Joe Biden D) Barack Obama")

if Q3 == ("D"): 
    scoreboard = scoreboard + 1
    print("That's correct! Your score: " + str(scoreboard)) 
 
else:
    print("That's incorrect")

Q4 = input("Before independence, what was Bangladesh called? A) East Pakistan B) Formosa C) Ceylon D) USA")

if Q4 == ("A"): 
    scoreboard = scoreboard + 1
    print("That's correct! Your score: " + str(scoreboard)) 
 
else:
    print("That's incorrect")

Q5 = input("How many floors does the school consist of? A) 1 B) 3 C) 2 D) 5")

if Q5 == ("C"): 
    scoreboard = scoreboard + 1
    print("That's correct! Your score: " + str(scoreboard)) 
 
else:
    print("That's incorrect")

print("You got a " + str(scoreboard) + "/5")