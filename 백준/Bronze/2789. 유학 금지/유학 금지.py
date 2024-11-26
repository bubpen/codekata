s = 'CAMBRIDGE'
i = input()
l = []
for w in i:
    if w not in s and w not in s.lower():
        l.append(w)
print(''.join(l))