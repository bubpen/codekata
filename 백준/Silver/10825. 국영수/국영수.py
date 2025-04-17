n = int(input())
array = []
for i in range(n):
    name, korean, english, math = input().split()
    array.append((name, int(korean), int(english), int(math)))
array.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for i in array:
    print(i[0])