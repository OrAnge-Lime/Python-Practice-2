step = int(input())
text = input()
text = text.lower()
text1 = ''
alfabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in text:
    if alfabet.__contains__(i):
        text1 += alfabet[(alfabet.find(i) + step) % alfabet.__len__()]
    else:
        text1 += i
print(text1)

