names = []
for _ in range(3):
    names.append( input("What's your name? "))
for name in sorted(names):#Sorted fuunction sort the names in  alphabatic order
    print(f"Hello {name}")
    