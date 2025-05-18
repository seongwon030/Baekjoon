import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def go(x,y, visited):
    global count
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or graph[x][y] == 0:
        return

    visited[x][y] = True
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        go(nx, ny, visited)

    return count

T = int(input())

for i in range(T):
    m,n,k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        a,b = map(int, input().split())
        graph[b][a] = 1

    all_counts = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1 and not visited[x][y]:
                count = 0
                go(x,y,visited)
                all_counts.append(count)

    print(len(all_counts))