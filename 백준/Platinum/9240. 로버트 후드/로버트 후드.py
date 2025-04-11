import sys
input = sys.stdin.readline

def ccw(p1,p2,p3):
  return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])


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



def rotating_calipers(points):
  n = len(points)
  if n == 2:
    return distance(points[0], points[1])
  
  max_distance = 0
  j = 1
  for i in range(n):
    ni = (i+1) % n
    while True:
      nj  = (j+1) % n
      d1 = distance(points[i], points[j])
      d2 = distance(points[i], points[nj])
      if d2 > d1:
        j = nj
      else:
        break
    max_distance = max(max_distance, distance(points[i], points[j]))

  return max_distance


def distance(p1,p2):
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5


n = int(input())
ans = 0
points = []
for _ in range(n):
  points.append(list(map(int, input().split())))

convex_arr = convex(points)
if len(convex_arr) == 1:
  print(0)
else:
  result = rotating_calipers(convex_arr)
  print(result)