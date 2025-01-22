string = "The new Boeing 777X will be the world’s largest and most efficient twin-engine jet, unmatched in every aspect of performance. With new breakthroughs in aerodynamics and engines, the 777X will deliver 10 percent lower fuel use and emissions and 10 percent lower operating costs than the competition. A true family, the 777X offers low-risk, profitable growth, industry-leading reliability and seamless integration with the 777 and 787 Dreamliner families for even more flexibility. But performance is just part of the story. With a spacious, wide cabin, new custom architecture and innovations from the 787 Dreamliner, the 777X will deliver the flight experience of the future."

def word_counter(string):
    count = 0
    for word in string.split():
        count += 1
    return count

word_counter(string)

def letter_count(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count