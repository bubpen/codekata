def solution(i, j, k):
    cnt = 0
    for i in range(i,j+1):
        for j in range(len(str(i))):
            if int(str(i)[j]) == k:
                cnt +=1 
    return cnt