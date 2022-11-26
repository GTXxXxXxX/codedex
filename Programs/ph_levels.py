ph = float(input("Insert a pH level (0 to 14): "))

if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")
