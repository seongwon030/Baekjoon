# 수정 후
from collections import deque

def bfs(original, x, y):
    max_len = 1
    q = set([(x, y, original[y][x])])  
    while q:
        x, y, alpha = q.pop()  
        max_len = max(max_len, len(alpha))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and original[ny][nx] not in alpha:
                q.add((nx, ny, alpha + original[ny][nx]))  
    return max_len

r, c = map(int, input().split())
original = []
for _ in range(r):
    original.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(bfs(original, 0, 0))