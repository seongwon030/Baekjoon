
def leftOrRight(left, mid, right):
  lx, ly = left
  rx, ry = right
  mx, my  = mid

  cross = (mx-lx) * (ry-ly) - (rx-lx) * (my-ly)

  if cross > 0:
    return "left" 
  elif cross < 0:
    return "right"
  else:
    return "colinear"

p1_x, p1_y = map(int, input().split())
p2_x, p2_y = map(int, input().split())
p3_x, p3_y = map(int, input().split())

result = leftOrRight((p1_x, p1_y), (p2_x, p2_y), (p3_x, p3_y))

if result == 'right':
  print(-1)
elif result == 'left':
  print(1)
else:
  print(0)

