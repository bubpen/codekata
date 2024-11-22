array = []
for i in range(9):
    array.append(int(input()))
max_num = max(array)
print(max_num)
print(array.index(max_num)+1)