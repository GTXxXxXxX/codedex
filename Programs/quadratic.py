a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))

root1 = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
root2 = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)

print(root1)
print(root2)
