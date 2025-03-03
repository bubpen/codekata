def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                num = nums[i]+nums[j]+nums[k]
                div = 0
                for _ in range(1,int(num**0.5)+1):
                    if num % _ ==0:
                        div +=1
                        if div > 1:
                            break
                if div == 1:
                    answer +=1
    return answer