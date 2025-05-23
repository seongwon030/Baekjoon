import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(u,path):
    global distance, leaf

    if distance < path:
        distance = path
        leaf = u

    visited[u] = 1

    for v,w in tree[u]:
        if visited[v] == 0:
            dfs(v, path+w)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n):
    arr = list(map(int, input().split()))
    i = arr[0]
    j = 1
    while True:
        tree[i].append((arr[j], arr[j+1]))
        tree[arr[j]].append((i, arr[j+1]))
        if arr[j+2] == -1:
            break
        j+=2

distance = 0
leaf = -1
visited = [0] * (n+1)
dfs(1,0)

visited = [0] * (n+1)
dfs(leaf,0)

print(distance)