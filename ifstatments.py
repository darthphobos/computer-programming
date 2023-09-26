salary = int(input("What is your salary? "))
years = int(input("How many years have you worked here? "))

if years >= 5:
    print(f"Your bonus will be{salary * 0.05}")
else:
    print("You do not qualify for a bonus.")

