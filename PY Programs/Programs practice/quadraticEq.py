import cmath
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
root = b**2 -4*a**c
root1 = (-b + cmath.sqrt(root))/(2*a)
root2 = (-b - cmath.sqrt(root))/(2*a)

print(root1)
print(root2)