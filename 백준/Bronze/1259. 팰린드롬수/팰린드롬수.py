while True:
    num = str(int(input()))
    reverse_num = ""
    if num == '0':
        break
    else:
        for i in range(0,len(num)):
            reverse_num = num[i] + reverse_num

    if reverse_num == num:
        print('yes')
    else:
        print('no')
