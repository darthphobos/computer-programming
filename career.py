userinput1 = input("Welcome to the interview what is your name? ")

print(f"Hello {userinput1}")

userinput2 = input("Ok what career are you interested in this field: Manager, Team leader, Senior Dev, Junior Dev? ")

userinput3 = int(input("What are your years of experience in programming? "))
if userinput2 == "Manager" or userinput2 == "manager":
    if userinput3 < 7:
        print("Sorry you don't have enough experience for this career right now. Please apply later.")
        exit()
elif userinput2 == "Team leader" or userinput2 == "team leader":
    if userinput3 < 5:
        print("Sorry you don't have enough experience for this career right now. Please apply later.")
        exit()
elif userinput2 == "Senior dev" or userinput2 == "senior dev":
    if userinput3 < 10:
        print("Sorry you don't have enough experience for this career right now. Please apply later.")
        exit()
elif userinput2 == "Junior dev" or userinput2 == "junior dev":
    if userinput3 < 1:
        print("Sorry you don't have enough experience for this career right now. Please apply later.")
        exit()

userinput4 = input("What is your desired salary? ")
if userinput3 == "Manager" or userinput3 == "manager":
    if userinput4 == 100:
        print("since you are a manager your salary is 100k")
elif userinput3 == "Team leader" or "team leader":
    print("since you are team leader you get 90k")
elif userinput3 == "Senior dev" or "senior dev":
    print("since you are team leader you get 120k")
elif userinput3 == "Junior dev" or "junior dev":
    print("since you are team leader you get 75k")

userinput5 = input("Tell me about your hobbies? ")

userinput6 = input("Do you have a crimnal record? if so tell me what crimes you have commited? ")

userinput7 = input("What do you want to contribit to this company or what is your vision? ")

userinput8 = input("Do you dislike animals? if so why is that? ")

userinput9 = input("Do you know muiltple coding languages? ")

userinput10 = input("What did you want to be growing up as a child? ")