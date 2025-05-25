# i = 1
# while i<=3:
#     print("meow")
#     i +=1

# for i in [0,10]:#List
#     print(i,"meow")
# for i in range(10):
#     print(i,"meow")
# for i in range(0,5):
#     print(i,"meow")
# num = int(input("How many times you want to print meow? "))
# print("meow\n"*num,end ="")

# while True:
#     n = int(input("What's n? "))
#     if n>0:
#         break
# for i in range(n):
#     print(i,"meow")

def main():
    num   = get_num();
    meow(num)
def get_num():
     while True :
        num = int(input("What's the number? "))
        if num>0:
            return num    
def meow(n):
     for _ in range(n): 
          print("meow")

main()