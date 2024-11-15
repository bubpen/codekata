dwarf = []

for i in range(9):
    d = int(input())
    dwarf.append(d)
dwarf.sort()
a = sum(dwarf)
s=[]
for i in range(len(dwarf)):
    for j in range(i+1,len(dwarf)):
        if a - dwarf[i] - dwarf[j] ==100:
            s.append((dwarf[i], dwarf[j]))
            break
c = [i for i in dwarf if i not in s[0]]
for i in c:
    print(i)