while True:
    sentence = input().lower()
    cnt = 0
    if sentence == '#':
        break
    else:
        for word in sentence:
            if word in ['a','e','i','o','u']:
                cnt += 1
        print(cnt)