from collections import deque

n = int(input())
k = list(map(int, input().split()))

cur, jump = 0, 0
queue = deque()
queue.append((cur, jump))  # 현재 인덱스, 점프 인덱스
visited = []

while queue:
    cur, jump = queue.popleft()
    if cur == len(k) - 1:  # 현재 인덱스가 마지막 칸에 해당하면 jump출력 후 종료
        print(jump)
        exit()

    for i in range(1, k[cur] + 1):  # k안에 있는 숫자 이하만큼 오른쪽으로 점프 가능
        next = cur + i
        if next not in visited:
            visited.append(next)
            if next == len(k) - 1:  # 다음 인덱스가 마지막 칸이면 jump출력 후 종료
                print(jump + 1)
                exit()
            queue.append((next, jump + 1))

print(-1)
