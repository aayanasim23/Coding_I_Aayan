def piglatin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0].lower() in vowels:
        return word + 'hay'
    else:
        return word[1:] + word[0] + 'ay'

piglatin("aayan")