import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V,E = map(int,input().split())
root = [i for i in range(V+1)]
edge = [] # 간선리스트
for i in range(E): 
  edge.append(list(map(int,input().split())))

# 비용을 기준으로 오름차순
edge.sort(key=lambda x:x[2])

def find(x):
  if x!=root[x]:
    root[x] = find(root[x])
  return root[x]

def union(a,b):
  a = find(a)
  b = find(b)
  if a<b:
    root[b] = a
  else:
    root[a] = b

ans = 0 
for a,b,c in edge:
  aRoot = find(a)
  bRoot = find(b)
  if aRoot != bRoot:
    union(aRoot,bRoot)
    ans+=c

print(ans) 