r, c = map(int, input().split())

k = [list(input()) for _ in range(r)]

ans = 0
alpha = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not k[nx][ny] in alpha:
            alpha.add(k[nx][ny])
            dfs(nx, ny, count+1)
            alpha.remove(k[nx][ny])

alpha.add(k[0][0])
dfs(0, 0, 1)
print(ans)