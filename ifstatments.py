# salary = int(input("What is your salary? "))
# years = int(input("How many years have you worked here? "))

# if years >= 5:
#     print(f"Your bonus will be{salary * 0.05}")
# else:
#     print("You do not qualify for a bonus.")

# length = int(input("What is the length of two lines in the rectangle? "))
# width = int(input("What is the width of the rectangle? "))

# if length == width:
#     print("This is a square. ")
# else:
#     print("This is not a square. ")

value1 = int(input("What is the first value? "))
value2 = int(input("What is the second value? "))

if value1 > value2:
    print("The first number is greater than the second number. ")
else:
    print("The first number is less than the second number. ")

age1 = int(input("What is the first age? "))
age2 = int(input("What is the second age? "))
age3 = int(input("What is the third age? "))

if age1 > age2 and age1 > age3:
    print("Age 1 is greater than age 2 ")
else:
    print("Age 1 is less than age 3 ")

if age2 > age1 and age2 > age3:
    print("Age 2 is greater than age 1 ")
else:
    print("Age 2 is less than age 3 ")

if age3 > age1 and age3 > age2:
    print("Age 3 is greater than age 1 ")
else:
    print("Age 3 is less than age 2 ")

classes_missed = int(input("How many classes have you missed? "))
classes_attended = int(input("How many classes have you attended? "))

if (classes_missed / classes_attended) >= 0.75:
    print(f"Your attendance is {(classes_missed / classes_attended) * 100}%")
    print("You may take the exam")
else:
    print(f"Your attendance is {(classes_missed / classes_attended) * 100}%")
    print("You cannot attend the exam loser")