n, m = map(int, input().split())
x, y, d = map(int, input().split())
rooms = []
count = 0
for i in range(n):
    rooms.append(list(map(int, input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while True:
    if rooms[x][y] == 0:
        rooms[x][y] = 2
        count += 1
    
    cleand = False
    for _ in range(4):
        d = (d - 1) % 4
        next_x = x + dx[d]
        next_y = y + dy[d]
        if 0<= next_x < n and 0 <= next_y < m and rooms[next_x][next_y] == 0:
            x, y = next_x, next_y
            cleand = True
            break
    if not cleand:
        bx = x - dx[d]
        by = y - dy[d]
        if 0 <= bx < n and 0 <= by < m and rooms[bx][by] != 1:
            x, y = bx, by
        else:
            break
print(count)