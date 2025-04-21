n, m = map(int,input().split())
dnas = [input() for _ in range(n)]
dnas.sort()
answer = ''
for i in range(m):
    count = {"A" : 0, "C" : 0, "G" : 0, 'T' : 0}
    for dna in dnas:
        count[dna[i]] += 1
    sorted_count = sorted(count, key = lambda x: (-count[x], x))
    answer += sorted_count[0]
print(answer)
result = 0
for dna in dnas:
    for i in range(m):
        if answer[i] != dna[i]:
            result += 1
print(result)