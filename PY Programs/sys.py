import sys
try:
    print(f"Hello my name is ",sys.argv[1])
except IndexError:
    pass
# print(len(sys.argv)) 