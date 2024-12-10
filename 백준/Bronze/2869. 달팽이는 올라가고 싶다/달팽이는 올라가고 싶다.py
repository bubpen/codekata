A, B, V = map(int,input().split())
if (V-B) % (A-B) == 0:
    day = (V-B) // (A-B)
else:
    day = (V-B) // (A-B) + 1
print(day)