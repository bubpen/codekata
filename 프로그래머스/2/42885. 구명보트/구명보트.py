def solution(people, limit):
    answer = 0
    people.sort()
    lighter = 0
    heavier = len(people)-1
    while lighter <= heavier:
        if people[lighter] + people[heavier] <= limit:
            lighter += 1
            heavier -= 1
        else:
            heavier -= 1
        answer += 1
    return answer