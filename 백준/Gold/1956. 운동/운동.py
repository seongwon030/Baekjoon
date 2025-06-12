import sys
input = sys.stdin.readline

INF = float('inf')

V,E = map(int, input().split())

dist = [[INF]*V for _ in range(V)]

for i in range(V):
    dist[i][i] = 0

for _ in range(E):
    a,b,c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

for k in range(V): # 중간 정점: k
    for i in range(V): # 출발 정점: i
        for j in range(V): # 도착 정점: j
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = INF
for i in range(V):
    for j in range(V):
        if i==j:
            continue
        if dist[i][j] == INF or dist[j][i] == INF:
            continue
        ans = min(ans, dist[i][j] + dist[j][i])

if ans == INF:
    print(-1)
else:
    print(ans)