# -- define variables --

gryf = 0
rave = 0
huff = 0
slyt = 0

# -- First Question --

print(" Q1) Do you like Dawn or Dusk?")
print("     1) Dawn")
print("     2) Dusk")


ans = int(input(" "))

if ans == 1:

    gryf += 1
    rave += 1

elif ans == 2:

    huff += 1
    slyt += 1

else:
    print(" Wrong input")

# -- Second Question --

print(" Q2) When I’m dead, I want people to remember me as:")
print("     1) The Good")
print("     2) The Great")
print("     3) The Wise")
print("     4) The Bold")

ans2 = int(input(" "))

if ans2 == 1:

    huff += 1

elif ans2 == 2:

    slyt += 1

elif ans2 == 3:

    rave += 1

elif ans2 == 4:

    gryf += 1
else:
    print(" Wrong input")

# -- Third Question --

print(" Q3) Which kind of instrument most pleases your ear?")
print("     1) The violin")
print("     2) The trumpet")
print("     3) The piano")
print("     4) The drum")

ans3 = int(input(" "))
print(" ")

if ans3 == 1:

    slyt += 1

elif ans3 == 2:

    huff += 1

elif ans3 == 3:

    rave += 1

elif ans3 == 4:

    gryf += 1
else:
    print(" Wrong input")

# -- Final Answer --

if gryf >= huff and gryf >= rave and gryf >= slyt:
    print(" Gryffindor !")
elif huff >= gryf and huff >= rave and huff >= slyt:
    print(" Hufflepuff!")
elif rave >= gryf and rave >= huff and rave >= slyt:
    print(" Ravenclaw!")
elif slyt >= gryf and slyt >= rave and slyt >= huff:
    print(" Slytherin!")
else:
    print(" None")
