import heapq
import sys

input = sys.stdin.readline

v,e = map(int, input().split())
start_vertex = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])

def dijkstra(start,size):
    distance = [float('inf')] * (size+1)
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n,w in graph[node]:
            cost = dist + w
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q,[cost,n])

    return distance

d = dijkstra(start_vertex,v)

for i in range(1,v+1):
    if d[i] == float('inf'):
        print('INF')
    else:
        print(d[i])
