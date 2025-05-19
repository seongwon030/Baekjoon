import sys
sys.setrecursionlimit(10**6)
import math

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_unions(A):
    visited = [[False] * N for _ in range(N)]
    unions = []

    def dfs(x, y, union):
        visited[x][y] = True
        union.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(A[x][y] - A[nx][ny]) <= R:
                    dfs(nx, ny, union)

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = []
                dfs(i, j, union)
                if len(union) > 1:
                    unions.append(union)

    return unions


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

count = 0

while True:
    unions = find_unions(A)
    if not unions:
        break

    # 각 연합에 대해 평균 계산 및 적용
    for union in unions:
        total_population = sum(A[x][y] for x, y in union)
        avg_population = total_population // len(union)
        for x, y in union:
            A[x][y] = avg_population

    count += 1

print(count)
