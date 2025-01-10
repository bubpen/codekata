def solution(polynomial):
    l = list(polynomial.replace(" ",'').split('+'))
    x_sum = 0
    n_sum = 0
    for i in l:
        if i[-1] == 'x':
            if len(i) ==1:
                x_sum += 1
            else:
                x_sum += int(i[0:len(i)-1])
        else:
            n_sum += int(i)
    if x_sum == 0:
        return f'{n_sum}'
    elif x_sum != 0 and n_sum == 0:
        if x_sum == 1:
            return 'x'
        else:
            return f'{x_sum}x'
    else:
        if x_sum == 1:
            return f'x + {n_sum}'
        else:
            return f'{x_sum}x + {n_sum}'