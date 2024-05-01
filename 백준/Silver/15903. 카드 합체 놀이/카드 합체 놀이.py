from sys import stdin
import heapq

n,m = map(int, stdin.readline().split())

k=[]
a = [int(x) for x in stdin.readline().split()]

for i in a:
  heapq.heappush(k,i)

for i in range(m):
  card1 = heapq.heappop(k)
  card2 = heapq.heappop(k)
  heapq.heappush(k, card1+card2)
  heapq.heappush(k, card1+card2)

print(sum(k))