import sys
input = sys.stdin.readline

def ccw(left, mid, right):
  lx, ly = left
  rx, ry = right
  mx, my  = mid

  cross = (mx-lx) * (ry-ly) - (rx-lx) * (my-ly)

  return cross > 0

def convex_hull(positions):
  convex = []
  for p3 in positions:
    while len(convex) >= 2:
      p1, p2 = convex[-2], convex[-1]
      if ccw(p1,p2,p3): 
        # p1->p2->p3가 반시계면 멈춤
        break
      convex.pop() # 시계방향 또는 일직선이면 볼록 껍질에 포함 안 됨
    convex.append(p3)
  
  return len(convex)

ans = 0
n = int(input())
positions = []
for i in range(n):
  positions.append(list(map(int, input().split())))

positions = sorted(positions, key=lambda pos:(pos[0], pos[1]))
ans += convex_hull(positions)

positions.reverse()
ans += convex_hull(positions)

print(ans-2)