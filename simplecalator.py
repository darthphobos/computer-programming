user1 = int(input("type a number: "))
user2 = int(input("type a second number: "))
user3 = input("choose an operation (+, -, *, /): ")

def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1 / num2)

if user3 == '+':
    add(user1, user2)

if user3 == '-':
    subtract(user1, user2)

if user3 == '*':
    multiply(user1, user2)

if user3 == '/':
    divide(user1, user2)