num = input()
b_num = str(num)
if len(num) < 2:
    num = '0' + num
    b_num = '0' + b_num
new_num = 0
i = 0
while b_num != new_num:
    w_sum = str(int(num[0]) + int(num[1]))
    new_num = num[-1] + w_sum[-1]
    i += 1
    if len(new_num) < 2:
        new_num = '0' + new_num
    if b_num == new_num:
        print(i)
        break
    else:
        num = new_num