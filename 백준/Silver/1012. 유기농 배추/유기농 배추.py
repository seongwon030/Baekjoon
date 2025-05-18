import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def go(x,y, visited):
    global count
    if x < 0 or x >= N or y < 0 or y >= M or visited[x][y] or graph[x][y] == 0:
        return

    visited[x][y] = True
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        go(nx, ny, visited)

    return count

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        a,b = map(int, input().split())
        graph[b][a] = 1

    all_counts = []
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1 and not visited[x][y]:
                count = 0
                go(x, y, visited)
                all_counts.append(count)

    print(len(all_counts))