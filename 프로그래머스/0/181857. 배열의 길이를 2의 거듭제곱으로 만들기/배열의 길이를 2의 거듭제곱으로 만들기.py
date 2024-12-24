def solution(arr):
    i = 0
    while True:
        if len(arr) == 2**i or len(arr) == 2**(i+1):
            break
        elif len(arr) >2**(i+1):
            i += 1
        else:
            if len(arr) > 2**i:
                for n in range(2**(i+1) - len(arr)):
                    arr.append(0)
    return arr