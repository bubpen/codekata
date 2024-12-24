def solution(arr):
    answer = 0
    arr_1 = []
    while True:
        for i in arr:
            if i >= 50 and i % 2 == 0:
                arr_1.append(i//2)
            elif i <50 and i % 2 == 1:
                arr_1.append(2*i + 1)
            else:
                arr_1.append(i)
        if arr == arr_1:
            break
        else:
            arr = arr_1
            arr_1 = []
            answer += 1
    return answer