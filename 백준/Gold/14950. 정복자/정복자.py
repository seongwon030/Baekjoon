import sys
input = sys.stdin.readline

n,m,t = map(int,input().split())
root = [i for i in range(n+1)]
edge = [] # 간선리스트

for i in range(m):
  edge.append(list(map(int,input().split())))

# 비용을 기준으로 오름차순
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

    for j in range(m):
      edge[j][2] += t

print(ans)