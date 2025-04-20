from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = True

queue = deque()
queue.append((0,0,0,0))

while queue:
    x, y, used, dist = queue.popleft()

    if x == n - 1 and y == m - 1:
        print(dist+1)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 0 and not visited[nx][ny][used]:
                visited[nx][ny][used] = True
                queue.append((nx, ny, used, dist+1))
            elif maze[nx][ny] == 1 and used == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                queue.append((nx, ny, 1, dist+1))

else:
    print(-1)