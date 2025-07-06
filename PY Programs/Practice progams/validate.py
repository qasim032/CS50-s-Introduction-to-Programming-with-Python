# email = input("What is your email? ").strip()
# username,domain = email.split("@")
# if username and  domain.endswith(".edu"or".com"):
#     print("Valid")
# else:
#     print("Invalid")

import re 
email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(com|edu|pk|org|net|gov|info)$", email):
    print("Valid")
else:
    print("Invalid")