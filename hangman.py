import random

print("Welcome to the guessing Game")


word_list = ["Trojan", "Worm", "Malware", "Virus"]
secret_word = random.choice(word_list)
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)


guess = str(input("Guess a letter: ")).lower()


for position in range(len(secret_word)):
    letter = secret_word[position]
    if letter == guess:
        display_word[position] = letter
print(display_word)
