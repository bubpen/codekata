n, k = map(int, input().split())
coins = []
count = 0
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
for coin in coins:
    if k >= coin:
        count += k // coin
        k -= k // coin * coin
print(count)