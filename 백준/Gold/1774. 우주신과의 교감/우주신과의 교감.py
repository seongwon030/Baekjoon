# 이미 연결된 상태에서 시작
# 가중치는 없기에 추가할 때마다 계산
# 좌표 하나를 하나의 정점으로 설정

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[x_root] = y_root
        return True
    return False

n,m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    union(a-1, b-1)

edges = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
        edges.append((dist, i, j))

edges.sort()
total = 0

for dist, i, j in edges:
    if union(i,j):
        total += dist

print(f"{total:.2f}")