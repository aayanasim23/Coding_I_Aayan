secret_word = "skull"

def get_guess():
    guess = input("Guess a word: ")

    while not (len(guess) == 1 and guess.islower()):
        print("Try Again!")
        guess = input("Guess a word: ")
    if guess in secret_word:
        return guess

print("You guessed:", get_guess())

def play_game():
    attempts = 10
    while attempts > 0:
        guess = get_guess()

        if guess == secret_word:
            print("Congrats! You guessed the word!")
            return

        print(f"Wrong guess. {attempts - 1} attempts left.")
        attempts -= 1

    print("Game Over! The secret word was:", secret_word)

play_game()