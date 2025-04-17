M, N = map(int, input().split())

num_to_eng = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

# 숫자와 해당 영어 표현을 튜플로 저장
numbers = []
for i in range(M, N + 1):
    eng = ' '.join([num_to_eng[int(d)] for d in str(i)])
    numbers.append((eng, i))

# 영어 표현을 기준으로 정렬
numbers.sort()

# 정렬된 숫자를 출력 (한 줄에 10개씩)
for idx, (_, num) in enumerate(numbers):
    print(num, end=' ')
    if (idx + 1) % 10 == 0:
        print()