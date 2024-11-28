while True:
    a = list(map(int,input().split()))
    if a[0]==a[1]==a[2]==0:
        break
    else:
        if a[1]-a[0]==a[2]-a[1]:
            print('AP',a[2]+(a[1]-a[0]))
        elif a[1]//a[0] == a[2]//a[1]:
            print('GP',a[2]*(a[1]//a[0]))