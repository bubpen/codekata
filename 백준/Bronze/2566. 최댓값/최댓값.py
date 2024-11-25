m = 0
w = [0, 0]
for i in range(9):
    numbers = list(map(int,input().split()))
    if max(numbers) >= m:
        m = max(numbers)
        w[0] = i+1
        w[1] = numbers.index(m)+1

print(m)
print(f'{w[0]}'+' '+f'{w[1]}')