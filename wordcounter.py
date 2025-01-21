def word_counter(string):
    count = 0
    for word in string.split():
        count += 1
    return count

word_counter('I am, a banana')

