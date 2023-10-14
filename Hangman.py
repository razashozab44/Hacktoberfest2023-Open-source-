import random

def get_random_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = get_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while True:
        print(f"\nAttempts left: {attempts}")
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess not in word_to_guess:
                attempts -= 1

        if "_" not in display_word(word_to_guess, guessed_letters):
            print(f"\nCongratulations! You guessed the word: {word_to_guess}")
            break
        elif attempts == 0:
            print(f"\nYou're out of attempts. The word was: {word_to_guess}")
            break

if __name__ == "__main__":
    hangman()
