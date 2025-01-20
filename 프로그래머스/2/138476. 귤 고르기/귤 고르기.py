def solution(k, tangerine):
    cnt ={}
    for i in tangerine:
        cnt[i] = cnt.get(i, 0) + 1
    diff = max(cnt.values())
    keys = []
    while k > 0:
        for key, value in cnt.items():
            if value == diff:
                keys.append(key)
                k -= diff
            if k <= 0:
                break
        diff -= 1
    return len(keys)