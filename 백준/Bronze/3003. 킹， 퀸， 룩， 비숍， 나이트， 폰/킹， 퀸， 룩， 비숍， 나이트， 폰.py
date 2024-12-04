chess_number = [1, 1, 2, 2, 2,8]
now_list = list(map(int,input().split()))
need_list = []
for i in range(len(chess_number)):
    need_list.append(str(chess_number[i] - now_list[i]))
print(' '.join(need_list))