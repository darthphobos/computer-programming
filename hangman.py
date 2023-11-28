
import random 
   
with open("sowpods.txt", "r") as file: 
    allText = file.read() 
    words = list(map(str, allText.split())) 
  
    # print random string 
    print(random.choice(words)) 
    
word = random.choice(words)
guessed = "_" * len(word)
word = list(word)
guessed = list(guessed)
listGuessed = []
letter = input("guess letter: ").upper()
lives = 10 
while True:
    if letter in listGuessed:
        letter = ""
        print("Already guessed!!")
    elif letter in word: 
        index = word.index(letter)
        guessed[index] = letter
        word[index] = '_'
    else:
        print(''.join(guessed))
        if letter != '':
            listGuessed.append(letter)
        letter = input("guess letter: ").upper()
    
    if letter not in guessed:
        lives -= 1
        print(f"You have {lives} lives left")
    
    if '_' not in guessed:
        print("YOU WON")
        print(f"Your word was: {''.join(guessed)}")
        exit()
    
    if lives == 0:
        print("Your a skill issue")
        exit()