import sys
input = sys.stdin.readline

def ccw(left, mid, right):
  lx, ly = left
  rx, ry = right
  mx, my  = mid

  cross = (mx-lx) * (ry-ly) - (rx-lx) * (my-ly)

  return cross

def is_cross(a1,a2,b1,b2):
  ab = ccw(a1,a2,b1) * ccw(a1,a2,b2)
  cd = ccw(b1,b2,a1) * ccw(b1,b2,a2)

  if ab == 0 and cd == 0:
    # 좌표 정렬: x 기준, x 같으면 y 기준
    def ordered(p1, p2):
      return (p1, p2) if p1 <= p2 else (p2, p1)

    a1, a2 = ordered(a1, a2)
    b1, b2 = ordered(b1, b2)

    # 겹치는 구간이 있는지 체크
    return not (a2[0] < b1[0] or b2[0] < a1[0] or
                (a2[0] == b1[0] and a2[1] < b1[1]) or
                (b2[0] == a1[0] and b2[1] < a1[1]))
  return ab <= 0 and cd <= 0 # 선분 양쪽에 두 점이 있을 때 교차한다

def get_intersection(a1,a2,b1,b2):
  A1 = a2[1] - a1[1]
  B1 = a1[0] - a2[0]
  C1 = A1 * a1[0] + B1 * a1[1]

  A2 = b2[1] - b1[1]
  B2 = b1[0] - b2[0]
  C2 = A2 * b1[0] + B2 * b1[1]

  det = A1 * B2 - A2 * B1
  if det == 0:
    return None
  else:
    x = (B2 * C1 - B1 * C2) / det
    y = (A1 * C2 - A2 * C1) / det
    return (x, y)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a1 = (x1,y1)
a2 = (x2,y2)
b1 = (x3,y3)
b2 = (x4,y4)

if is_cross(a1, a2, b1, b2):
    print(1)
    point = get_intersection(a1, a2, b1, b2)
    if point:  # 격자점 교차
        x, y = point
        print(f"{int(x) if x.is_integer() else f'{x:.10f}'} {int(y) if y.is_integer() else f'{y:.10f}'}")
    else:
        # 겹치는 경우일 때 출력: 교차하는 한 점(공통 부분 중 가장 작은 점)
        candidates = sorted([a1, a2, b1, b2])
        # 네 점 중 겹치는 구간: max(mins), min(maxs)
        start = max(min(a1, a2), min(b1, b2))
        end = min(max(a1, a2), max(b1, b2))
        if start == end:
            print(*start)
else:
    print(0)