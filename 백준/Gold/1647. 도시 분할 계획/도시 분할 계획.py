import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V,E = map(int,input().split())
root = [i for i in range(V+1)]
edge = [list(map(int,input().split())) for i in range(E)]

edge.sort(key=lambda x:x[2])

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

ans = 0
mst_edges = []
degree = [0] * (V+1)
for a,b,c in edge:
    aRoot = find(a)
    bRoot = find(b)
    if aRoot != bRoot:
        if aRoot > bRoot:
            root[aRoot] = bRoot
        else:
            root[bRoot] = aRoot
        ans += c
        mst_edges.append([a,b,c])
        degree[a] += 1
        degree[b] += 1

mst_edges.sort(key=lambda x:x[2], reverse=True)
for a,b,c in mst_edges:
    if degree[a] >= 1 and degree[b] >= 1:
        ans -= c
        break

print(ans)