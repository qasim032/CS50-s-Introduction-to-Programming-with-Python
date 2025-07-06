# name = input("What's your name? ")
# file  = open("name.txt","a")
# file.write(name+"\n")
# name = input("What's your name? ")
# with  open("name.txt","a") as file:
#     file.write(name+"\n")
with open("name.txt","r") as file:
    line = file.readlines()
for name in line:
    print(f"Hello {name}",end="") 
#or#print("Hello",name.rstrip())
 



