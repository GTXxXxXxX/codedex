# # Codédex solution

# import random

# question = input("Question: ")

# random_number = random.randint(1, 9)
# # print(random_number)

# if random_number == 1:
#     answer = "Yes - definitely"
# elif random_number == 2:
#     answer = "It is decidedly so"
# elif random_number == 3:
#     answer = "Without a doubt"
# elif random_number == 4:
#     answer = "Reply hazy, try again"
# elif random_number == 5:
#     answer = "Ask again later"
# elif random_number == 6:
#     answer = "Better not tell you now"
# elif random_number == 7:
#     answer = "My sources say no"
# elif random_number == 8:
#     answer = "Outlook not so good"
# elif random_number == 9:
#     answer = "Very doubtful"
# else:
#     answer = "Error"

# print("Question:      " + question)
# print("Magic 8 Ball:  " + answer)

# --------------------------------------------------------------------------------------------------------------------------------------------------

import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes – definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes Signs point to yes",
    "Reply hazy",
    "try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Dont count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

print("  __  __          _____ _____ _____    ___  ")
print(" |  \/  |   /\   / ____|_   _/ ____|  / _ \ ")
print(" | \  / |  /  \ | |  __  | || |      | (_) |")
print(" | |\/| | / /\ \| | |_ | | || |       > _ < ")
print(" | |  | |/ ____ \ |__| |_| || |____  | (_) |")
print(" |_|  |_/_/    \_\_____|_____\_____|  \___/ ")
print("")
print("")
print("")
print("Hello World, I am the Magic 8 Ball, What is your name?")
name = input()
print("hello " + name)


def Magic8Ball():
    print("Ask me a question.")
    input()
    print(answers[random.randint(0, len(answers) - 1)])
    print("I hope that helped!")
    Replay()


def Replay():
    print("Do you have another question? [Y/N] ")
    reply = input()
    if reply == "Y":
        Magic8Ball()
    elif reply == "N":
        exit()
    else:
        print("I apologies, I did not catch that. Please repeat.")
        Replay()


Magic8Ball()
