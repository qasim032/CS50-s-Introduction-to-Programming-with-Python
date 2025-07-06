# languages = {
#     'jen' : 'python',
#     'jack':'java'
# }
# for name,lan in languages.items():
#     print(f"{name} uses {lan}")
    
    
# print('\n\n\n')
# li1 = {'green':5,'red':3,}
# li2 = {'river':5,'oceans':6}
# all = [li1,li2]
# i=1
# for lists in all:
#     print(f"list no #{i}")
#     i=i+1
#     for data in lists:
#         print(f"{data} contains {lists[data]} letters")
        
#     print()

dictionaryy ={
    "One":1,
    "Two":2,
    "Three":3
}
keys = list(dictionaryy)
print(keys)
for j in range(len(dictionaryy)):
    print(j,f"{keys[j]}: {dictionaryy[keys[j]]}")
print(type(keys))