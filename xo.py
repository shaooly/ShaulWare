#להסביר שימוש של סלאש n לצורך ירידת שורה
word = input("Please insert word:\n")
show_word = '_' * len(word)
print('\n' * 100)
guesses = 5
# שימוש במנה נתונים set
guessed_letters = set()

while True:
    guess = input(f'Guess a letter or a word ( allready guesses{guessed_letters}): {show_word}\n')
    if len(guess) == 1: # ניחשו אות
        guessed_letters.add(guess)
        show_word = ''
        for c in word:
            if c in guessed_letters:
                show_word += c
            else:
                show_word += '_'
        if '_' not in show_word:
            print(f'You completed the word {word}')
            break
    if len(guess) > 1: # ניחשו מילה
        if guess == word:
            print(f'You guesses the word {word}')
            break
        else:
            print(f'Sorry, the word {guess} is incorrect')
    guesses -= 1
    if not guesses:
        print(f'Game Over. The word was {word}')
        break