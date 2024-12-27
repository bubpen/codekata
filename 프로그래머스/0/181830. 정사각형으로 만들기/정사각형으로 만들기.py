def solution(arr):
    s = len(arr[0])
    h = len(arr)
    if s == h:
        pass
    elif h < s:
        for i in range(s-h):
            arr.append([0]*s)
    elif s < h:
        for i in range(h):
            for j in range(h - len(arr[i])):
                arr[i].append(0*(h-s))
    return arr