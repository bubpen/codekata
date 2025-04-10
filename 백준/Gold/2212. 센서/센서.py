n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
diff = [sensors[i] - sensors[i-1] for i in range(1, n)]
cut = []
cut = sorted(range(len(diff)), key=lambda i: diff[i], reverse=True)[:k-1]
cut = [i+1 for i in cut]
cut.sort()
sets = []
last = 0
for i in cut:
    sets.append(sensors[last:i])
    last = i
sets.append(sensors[last:])
answer = 0
for set in sets:
    answer += max(set)-min(set) if set else 0
print(answer)