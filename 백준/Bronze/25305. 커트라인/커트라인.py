n, m = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
print(s[-m])