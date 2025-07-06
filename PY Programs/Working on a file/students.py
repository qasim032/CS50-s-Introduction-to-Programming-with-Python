# with open("name.csv") as file:
#     for line in file :
#         name,house = line.split(",")
#         print(name+" lives in ",house,end="")
# with open("name.csv","a") as file:
#     name = input("What's your name? ")
#     house = input("Where do you live ? ")
#     file.write(name+","+house)




# students = []
# with open("name.csv")as file:
#     for info in file:
#         name,house = info.split(",")
#         students.append(name+","+house)
# for student in students:
#     name,house= student.split(",")
#     print(name)


# import csv
# name  = input("What's your name? ")
# home = input("Where do you live? ")
# with open("name.csv","a",newline="") as file:
#     writer  = csv.writer(file)
#     writer.writerow([name,home])

import csv
name  = input("What's your name? ")
home = input("Where do you live? ")
with open("name.csv","a",newline="") as file:
    writer  = csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})
