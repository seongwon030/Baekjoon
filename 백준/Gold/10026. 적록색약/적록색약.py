import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def find_RGB(color, x, y, visited):
    global count
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
        return

    if graph[x][y] != color:
        return

    visited[x][y] = True
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        find_RGB(color, nx, ny, visited)

    return count

def not_find_RGB(color, x, y, visited):
    global count
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
        return

    if color == 'R':
        if graph[x][y] == 'B':
            return

    elif color == 'G':
        if graph[x][y] == 'B':
            return

    else:
        if color != graph[x][y]:
            return

    visited[x][y] = True
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        not_find_RGB(color, nx, ny, visited)

    return count

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().strip()))

visited = [[False] * n for _ in range(n)]

RGB_list = []
for x in range(n):
    for y in range(n):
        count = 0
        if not visited[x][y]:
            if graph[x][y] == 'R':
                find_RGB(graph[x][y], x, y, visited)

            elif graph[x][y] == 'G':
                find_RGB(graph[x][y], x, y, visited)

            elif graph[x][y] == 'B':
                find_RGB(graph[x][y], x, y, visited)

            RGB_list.append(count)

print(len(RGB_list) , end = ' ')

not_RGB_list = []
visited = [[False] * n for _ in range(n)]

for x in range(n):
    for y in range(n):
        count = 0
        if not visited[x][y]:
            if graph[x][y] == 'R':
                not_find_RGB(graph[x][y], x, y, visited)

            elif graph[x][y] == 'G':
                not_find_RGB(graph[x][y], x, y, visited)

            elif graph[x][y] == 'B':
                not_find_RGB(graph[x][y], x, y, visited)

            not_RGB_list.append(count)

print(len(not_RGB_list))
