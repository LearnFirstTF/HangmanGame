import random

print("Welcome to guessing game!")

word_list = ["Trojan", "Worm", "Malware", "Virus"]
secret_word = random.choice(word_list)

print(secret_word)

guess = str(input("Enter your guess: "))

for letter in secret_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

print("this is my first project")
print("This is my first pull")
