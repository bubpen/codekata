expressions = list(input().split('-'))
result = []
for expression in expressions:
    num = 0
    for i in expression.split('+'):
        num += int(i)
    result.append(num)
answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]
print(answer)