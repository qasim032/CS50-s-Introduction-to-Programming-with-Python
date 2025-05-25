# name = input("What is your name ").strip().title()
# first,last = name.split()

# print(f"Hello,{nam}")


# def hello(name):
#     print("Hello",name)
# name = input("What's your name? ")
# hello(name)
#squaring a n number
def main():
    x = int(input("What's x? "))
    print("X square is ",square(x))
def square(x):
    return pow(x,2)
main()