word = "MARKARAGNOS"
guesses = "_ _ _ _ _ _ _ _ _ _ _"
win = False 
while win == False:
    loopword = "" 
    guess = input("Guess a ladder letter")
    if len(guess) > 1:
        if guess == word:
            win = True 
            break 
    if word.find(guess) != -1:
        for i in range(len(word)):
            if guess == word[i] or guesses.find(word[i]) > -1:
                loopword = loopword + word[i] + " "
            else:
                loopword = loopword + "_ "
    guesses = loopword
    print(guesses)

print("Go touch grass for wasting your time on this computer")