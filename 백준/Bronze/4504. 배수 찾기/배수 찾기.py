n = int(input())
b = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        b.append(a)
for i in b:
    if i % n == 0:
        print(i,'is a multiple of', f'{n}.')
    else:
        print(i, 'is NOT a multiple of', f'{n}.')