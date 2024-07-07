# 네트워크 연결 - 골드4
import sys
input = sys.stdin.readline

n = int(input()) # 정점의 개수
m = int(input()) # 간선의 개수
root = [i for i in range(n+1)]
edge = []

for i in range(m):
  edge.append(list(map(int,input().split())))

edge.sort(key=lambda x:x[2])

def find(x):
  if x!=root[x]:
    root[x] = find(root[x])
  return root[x]

ans = 0
for a,b,c in edge:
  aRoot = find(a)
  bRoot = find(b)
  if aRoot != bRoot:
    if aRoot > bRoot:
      root[aRoot] = bRoot
    else:
      root[bRoot] = aRoot
    ans += c

print(ans)