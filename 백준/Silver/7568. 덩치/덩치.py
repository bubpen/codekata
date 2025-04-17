n = int(input())
people =[]
for _ in range(n):
    w, h = map(int, input().split())
    people.append((w, h))
ranking=[]
for person in people:
    w, h = person[0], person[1]
    count = 1
    for other in people:
        if other==person:
            continue
        ow, oh = other[0], other[1]
        if ow>w and oh>h:
            count += 1
    ranking.append(str(count))
print(" ".join(ranking))