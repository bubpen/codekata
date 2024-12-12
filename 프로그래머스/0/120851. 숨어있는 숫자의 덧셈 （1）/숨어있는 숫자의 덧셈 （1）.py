def solution(my_string):
    answer = 0
    for i in my_string:
        if i.lower() in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            continue
        else:
            answer += int(i)
    return answer