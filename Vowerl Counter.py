vowels = "a e i o u"

def vowel_count(string):
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    
    return count

vowel_count("and")