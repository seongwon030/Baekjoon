from collections import deque
import sys

input = sys.stdin.readline

result, cnt = 0,0
MAX = 10**5 # 움직일 수 있는 최대좌표
dist = [0] * (MAX + 1) # 해당 위치에 도착했을 때 시간
n, k = map(int,input().split())

q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x==k: # x변수인 수빈의 위치가 동생이 있는 k와 같을 때 멈춤
      result = dist[x]
      cnt += 1
      continue
    # nx = 4,6,10 (현재 위치 5일 때 이동할 수 있는 방향)
    for nx in (x-1, x+1, x*2):
      # 범위내에 있고 아직 방문안했거나 이전 방문 + 1이 현재
      if 0 <= nx <= MAX and (not dist[nx] or dist[nx] == dist[x]+1):
        dist[nx] = dist[x] + 1  # 이동한 위치에 현재 이동한 시간 표시
        q.append(nx)

print(result)
print(cnt)