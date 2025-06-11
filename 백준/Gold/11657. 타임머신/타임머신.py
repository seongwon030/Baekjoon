import sys
input = sys.stdin.readline
INF = int(1e9)

V,E = map(int,input().split())
edges = [tuple(map(int,input().split())) for _ in range(E)]
dist = [INF] * (V+1)

def bellman_ford(start):
    dist[start] = 0
    for i in range(V):
        for j in range(E):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧을 때
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + cost:
                dist[next_node] = dist[cur_node] + cost
                if i == V-1:
                    return True
    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, V+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])