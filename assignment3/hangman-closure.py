def make_hangman(secret_word):
    guesses= []
    def hangman_closure(letter):
        guesses.append(letter)

        shown= "".join([cha if cha in guesses else "_" for cha in secret_word])
        print(shown)

        return all(cha in guesses for cha in secret_word)
    return hangman_closure

secret= input("Enter a secret word: ").lower()
guess = make_hangman(secret)

completed= False
while not completed:
    letter = input("Guess a letter: ").lower()
    completed = guess(letter)
print("Got it!")