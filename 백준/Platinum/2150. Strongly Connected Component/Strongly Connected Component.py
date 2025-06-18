import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n)]
reverse = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    reverse[v - 1].append(u - 1)

visited = [False] * n
stack = []

def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
    stack.append(v)

def reverse_dfs(v, result):
    visited[v] = True
    result.append(v)
    for u in reverse[v]:
        if not visited[u]:
            reverse_dfs(u, result)

for i in range(n):
    if not visited[i]:
        dfs(i)

visited = [False] * n
scc_list = []

while stack:
    v = stack.pop()
    if not visited[v]:
        result = []
        reverse_dfs(v, result)
        scc_list.append(sorted(result))

scc_list.sort(key=lambda x: x[0])

print(len(scc_list))
for scc in scc_list:
    print(*[v+1 for v in scc], -1)