a = input()
a1 = a.split(" ")
price = a1[-1]
list = []
for i in range(int(a1[0])):
    list.append(input())

summ = 0
positions = []
for i in range(list.__len__()):
    if int(list[i].split(" ")[0]) * int(list[i].split("*")[1].split(' ')[0]) != int(list[i].split('=')[-1]):
        positions.append(i+1)
    summ += int(list[i].split(" ")[0]) * int(list[i].split("*")[1].split(' ')[0])

print(int(a1[-1])-summ)
print(positions)