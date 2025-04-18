n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))
members.sort()
for member in members:
    print(member[0], member[2])