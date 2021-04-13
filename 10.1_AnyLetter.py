word = input()
num = int(input())
if  num > word.__len__() or num < 1:
    print("ОШИБКА")
else:
    print(word[num-1])
