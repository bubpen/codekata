payment = list(map(int, input().split()))
parking = []
out = []
for _ in range(3):
    s, e = map(int, input().split())
    parking.append(s)
    out.append(e)
last = max(out)
parkings = [[0, 0, 0] for _ in range(last)]
for i in range(3):
    s = parking[i]
    e = out[i]
    for j in range(last):
        if  s <= j < e:
            parkings[j][i] = 1
answer = 0
for i in range(last):
    count = parkings[i].count(1)
    if count == 1:
        answer += payment[0]
    elif count == 2:
        answer += payment[1] * 2
    elif count == 3:
        answer += payment[2] * 3
print(answer)