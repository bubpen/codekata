cards = [i for i in range(1,21)]
for i in range(10):
    a, b = map(int, input().split())
    cards[a-1:b] = cards[a-1:b][::-1]
for i in range(len(cards)):
    if i < len(cards)-1:
        print(cards[i], end = ' ')
    else:
        print(cards[i])