def solution(numbers):
    answer =[]
    i = 0
    while i < len(numbers):
        if numbers[i]=='o' and numbers[i+1]=='n':
            answer.append('1')
            i +=3
        elif numbers[i]=='t' and numbers[i+1]== 'w':
            answer.append('2')
            i +=3
        elif numbers[i]=='t' and numbers[i+1]== 'h':
            answer.append('3')
            i +=5
        elif numbers[i]=='f' and numbers[i+1]== 'o':
            answer.append('4')
            i += 4
        elif numbers[i]=='f' and numbers[i+1]== 'i':
            answer.append('5')
            i += 4
        elif numbers[i]=='s' and numbers[i+1]== 'i':
            answer.append('6')
            i += 3
        elif numbers[i]=='s' and numbers[i+1]== 'e':
            answer.append('7')
            i += 5
        elif numbers[i]=='e' and numbers[i+1]=='i':
            answer.append('8')
            i += 5
        elif numbers[i]=='n' and numbers[i+1]== 'i':
            answer.append('9')
            i += 4
        elif numbers[i]=='z' and numbers[i+1]== 'e':
            answer.append('0')
            i += 4
    return int(''.join(answer))