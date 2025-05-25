def main():
    x = get_x("What is x? ")
    print(f"x is {x}")
def get_x(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            print("X is not an integer. Please enter an integer:")
            continue
main()
        

