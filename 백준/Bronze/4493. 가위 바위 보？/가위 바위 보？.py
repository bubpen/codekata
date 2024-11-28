n = int(input())
for i in range(n):
    p = int(input())
    cnt1 = 0
    cnt2 = 0
    for j in range(p):
        p1,p2 = input().upper().split()
        if p1 == p2:
            cnt1 = cnt1
            cnt2 = cnt2
        elif (p1 == 'R' and p2 == 'S') or (p1 == 'S' and p2 == 'P') or (p1 == 'P' and p2 == 'R'):
            cnt1 += 1
        else:
            cnt2 +=1
    if cnt1 ==cnt2:
        print('TIE')
    elif cnt1 > cnt2:
        print('Player 1')
    else:
        print('Player 2')