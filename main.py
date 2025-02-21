# Mastermind game in Python
import random

# generates random code
secretCode = []
for i in range(0,4):
    n = random.randint(1,9)
    secretCode.append(str(n))

# displays sorted digits of code
print("Here are the digits that are valid guesses.")
for digit in sorted(secretCode):
    print(digit, end='')

# body for reading user guesses
guesses = 5
while guesses > 0:
    print("\nYou have", guesses, "guess(es) left.")
    userCode = list(str(input("Make your guess: ")))
    correct = 0
    # reads user's guess and determines how many digits are correct
    for i in range(0,4):
        if userCode[i] == secretCode[i]:
            correct+=1
    if correct == 4:
        print("You win!")
        break
    print("You have guessed", correct, "number(s) correctly")
    guesses-=1
    if guesses == 0:
        print("You lose! The secret code is: ", end='')
        for num in secretCode:
            print(num, end='')
        break
