sentence = input()
word = ''
sample = []
answer = 0
for i in sentence:
    if i == 'X':
        word += i
        if word == 'XXXX':
            sample.append('AAAA')
            word = ''
    elif i == '.':
        if word == 'XX':
            sample.append('BB')
            word = ''
        elif word:
            answer = -1
            break
        sample.append('.')
if word:
    if word == 'XX':
        sample.append('BB')
    else:
        answer = -1
if answer == -1:
    print(-1)
else:
    print(''.join(sample))