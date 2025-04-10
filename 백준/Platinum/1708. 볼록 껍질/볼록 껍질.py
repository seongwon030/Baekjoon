import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex(points):
  points = sorted(points)

  lower = []
  for p in points:
    while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0: # 일직선상도 가능
      lower.pop()
    lower.append(p)
  
  upper = []
  for p in reversed(points):
    while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
      upper.pop()
    upper.append(p)

  return lower[:-1] + upper[:-1]


n = int(input())

points = []
for i in range(n):
  points.append(list(map(int,input().split())))

result = convex(points)

print(len(result))