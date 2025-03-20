secret_word = "skull"

def get_guess():
    guess = input("Guess a letter: ")

    while not (len(guess) == 1 and guess.islower()):
        print("Try Again!")
        guess = input("Guess a letter: ")
    return(guess)



def update_dashes(guess, hanglist, secret_word):
    dashes_update = -1
    for letter in secret_word:
        dashes_update += 1
        if letter == guess:
            hanglist[dashes_update] = guess
        hanglist[0]


def play_game():
    attempts = 10
    hanglist = ['-', '-', '-', '-', '-']
    while attempts > 0:
        guess = get_guess() 

        if guess in secret_word:  
            print("Correct guess!")
            update_dashes(guess, hanglist, secret_word)
        else:
            print("Wrong guess.")
        print(hanglist)
        
        attempts -= 1
        print("Attempts left:", attempts)
       
        if ''.join(hanglist) == secret_word: #with the help of Dr. Lepat!
            print("You were correct!")
            break

    print("Game Over! The secret word was:", secret_word)

play_game()
