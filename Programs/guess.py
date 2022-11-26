import sys

guess = 0
tries = 0
print(" |====================|")
print(" | Guess the number ! |")
print(" |====================|")
print("")

while guess != 6:

    guess = int(input(" | Guess the number:  "))

    if guess != 6:
        tries += 1
        print(" You tried", tries, "time on 5 !")
    elif guess == 6:
        print(" You got it!")
    if tries >= 5:
        print(" You tried to much !")
        sys.exit()
