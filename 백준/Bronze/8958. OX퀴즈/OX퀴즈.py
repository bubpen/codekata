n = int(input())
for i in range(n):
    answer = input()
    result = 0
    correct = []
    for i in answer:
        if i == 'O':
            correct.append(i)
        elif i == 'X':
            correct = []
        result += len(correct)
    print(result)