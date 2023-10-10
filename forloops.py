from turtle import done


word = "paradigm"
for i in word:
    print(i)

list1 = [5,10,15,20]
list2 = ['tomatos', 'Potatos', 'carrots', 'cucmburs']

for i in list1:
    for j in list2:
        print(i, j)

for x in range(5):
    print(x)

list1 = ['Mango','Banana','Orange']
list2 = []

for i in list1:
    list2.append(i)

print(list2)

animal_list = ["cat", "dog", "tiger", "cow"]
for i in animal_list:
    print(i)

flowers = ['Jasmine','Lotus','Rose','Sunflower'] 
[print(x) for x in flowers]
if flowers:
    print("done")

vehicles = ['Car','Cycle','Bus','Tempo']
for char in vehicles:
    print(char)
    if char == 'Bus':
        break

vehicles = ['Car','Cycle','Bus','Tempo']
for char in vehicles:
    if char == 'Bus':
        continue
    print(char)

numbers = [12,3,56,67,89,90]
count = 0