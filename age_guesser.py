import random

print("Hi! I am going to try and guess your age...")
name = input("What's your name? ")

guessed_ages = []

while True:
    age = random.randint(15,40)

    if age in guessed_ages:
        continue

    while True:

        answer = input(f"Are you {age} years old? [Y/N]")

        if answer == "Y" or answer == "y" or answer == "yes" or answer =="Yes":
            guessed_ages.append(age)
            print("Easy! I'm a genius!")
            print(f"{name} is {age} years old.")
            break

        elif answer == "N" or answer == "n" or answer == "No" or answer == "no":
            guessed_ages.append(age)
            print("Rats.")
            break

        else:
            print("Please answer with the letters: [Y/N]")

    if answer == "Y" or answer == "y":
        break