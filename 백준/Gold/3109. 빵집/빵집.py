# 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선 이동 가능
# 마지막 열 도착했을 때 stop

# 모든 파이프라인은 첫 번째 열에서 시작되므로 밑으로 열번호 아래로 내리면서(인덱스 증가)진행
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R,C = map(int, input().split())
bread = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

# 가스를 최대한 많이 사용하려면 오른쪽 대각선위, 오른쪽, 오른쪽 대각선밑 순으로 탐색
dy = [-1,0,1]
answer = 0
def dfs(x,y):
    if y == C-1:
        return True
    for d in dy:
        nx = x + d
        ny = y + 1
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and bread[nx][ny] == '.':
                visited[nx][ny] = True
                if dfs(nx,ny):
                    return True
    return False

for i in range(R):
    if dfs(i,0):
        answer += 1


print(answer)