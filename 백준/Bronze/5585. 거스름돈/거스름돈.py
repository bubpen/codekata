coins = [500, 100, 50, 10, 5, 1]
pay = 1000
n = int(input())
change = pay - n
count = 0
for coin in coins:
    if change == 0:
        break
    if change >= coin:
        count += change // coin
        change %= coin
print(count)