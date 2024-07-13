from collections import deque
import sys

input = sys.stdin.readline

n,e = map(int,input().split())

indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(e):
  a,b = map(int,input().split())
  graph[a].append(b)
  indegree[b] += 1

def topology_sort():
  q = deque()
  result = []

  # 진입차수 0인 노드 탐색
  for i in range(1,n+1):
    if indegree[i] == 0: # 큐에 등록
      q.append(i)

  while q:
    now = q.popleft() # 선입선출
    result.append(now)
    for node in graph[now]: # 해당 노드와 연결된 노드들의 진입차수에서 1 빼기
      indegree[node] -= 1
      if indegree[node] == 0:
        q.append(node)
  
  for value in result:
    print(value,end=' ')

topology_sort()