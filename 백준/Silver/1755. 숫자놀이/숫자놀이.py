start, end = map(int, input().split())
array = [str(x) for x in range(start, end+1)]
number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = []
for i in array:
    number = []
    for j in i:
        number.append(number_words[int(j)])
    numbers.append(' '.join(number))
numbers.sort()
result = []
for i in numbers:
    num = ''
    for j in i.split():
        num += str(number_words.index(j))
    result.append(num)
for i in range(len(result)):
    if i % 10 == 9:
        print(result[i])
    else:
        print(result[i], end=' ')