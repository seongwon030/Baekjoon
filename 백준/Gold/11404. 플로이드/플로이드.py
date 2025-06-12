import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())
m = int(input())

dist = [[INF]*n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

for k in range(n): # 중간 정점: k
    for i in range(n): # 출발 정점: i
        for j in range(n): # 도착 정점: j
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for row in dist:
    print(' '.join(['0' if x == INF else str(x) for x in row]))