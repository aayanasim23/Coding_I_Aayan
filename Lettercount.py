def letter_count(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count

print(letter_count('banana', 'a'))