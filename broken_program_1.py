# A Very Broken Program 
#
# The following program is very buggy! It does not have the desired output.
# Can you identify the errors in the program and fix them?
#


# Part 1: A Broken Madlib

# The following lines should take input from the user and assign them to variables
place = input("Give me a place")
adjective = input("Give me an adjective")
emotion = input("Give me an emotion")
ing_verb = input("Give me a ing verb")
noun = input ("Give me a noun")

# The following should concatenate the variables above into lines in the Madlib
line1 = "Today, I went to " + place + " It was very " + adjective + "."
line2 = "When I arrived, I felt " + emotion
line3 = "I spent the day " + ing_verb + " to the " + noun + "."

# Then, print the lines of the Madlib
print(line1, line2, line3) 
