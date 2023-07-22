from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
k = list(map(int,input().split()))
a = deque([i for i in range(1,n+1)]) # 1부터 n까지 큐 생성 

cnt = 0
for i in k: # 추출할 수에 대해서 반복문 
  while True: # 첫번째 원소가 i면 뽑아내고 멈추기 
    if a[0] == i:
      a.popleft()
      break
    else:  
      if a.index(i) < len(a)/2:  # i의 인덱스가 큐 크기를 2로 나눈 것보다 작으면 왼쪽으로 이동 
        while a[0] != i:
          a.append(a.popleft())
          cnt+=1
      else:
        while a[0] != i:  # i의 인덱스가 큐 크기를 2로 나눈 것보다 크면 오른쪽으로 이동 
          a.appendleft(a.pop())
          cnt+=1
print(cnt)