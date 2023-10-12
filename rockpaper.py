user1 = input("Rock, paper or scissors? ")
user2 = input("Rock, paper or scissors? ")

if user1 == "Rock" or user1 == "rock":
    if user2 == "paper" or user2 == "Paper":
        print("user2 wins")
    elif user2 == "scissors" or user2 == "Scissors":
        print("user1 wins")
    elif user2 == "Rock" or user2 == "rock":
        print("you chose the same try again")

if user1 == "Paper" or user1 == "paper":
    if user2 == "paper" or user2 == "Paper":
        print("you chose the same try again")
    elif user2 == "scissors" or user2 == "Scissors":
        print("user2 wins")
    elif user2 == "Rock" or user2 == "rock":
        print("user1 wins")