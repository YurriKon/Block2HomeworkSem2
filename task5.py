# Реализуйте алгоритм перемешивания списка.
import random

a = ['Шла', 'Саша', 'по', 'шоссе']
for i in a:
    print(i, end = ' ')
print()
print('====================')
b = list(a)
random.shuffle(b)
count = 1
while b != a:
    print(count, end = ': ')
    random.shuffle(b)
    for i in b:
        print(i, end = ' ')
    count += 1
    print()
        


