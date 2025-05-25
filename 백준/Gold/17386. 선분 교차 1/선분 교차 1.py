import sys
input = sys.stdin.readline

def ccw(a, b, c):
    return (b[0]-a[0]) * (c[1]-a[1]) - (b[1]-a[1]) * (c[0]-a[0])

def is_cross(a1, a2, b1, b2):
    ab = ccw(a1, a2, b1) * ccw(a1, a2, b2)
    cd = ccw(b1, b2, a1) * ccw(b1, b2, a2)

    if ab == 0 and cd == 0:
        a1, a2 = sorted([a1, a2])
        b1, b2 = sorted([b1, b2])
        return not (a2 < b1 or b2 < a1)
    return ab <= 0 and cd <= 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a1 = (x1, y1)
a2 = (x2, y2)
b1 = (x3, y3)
b2 = (x4, y4)

print(1 if is_cross(a1, a2, b1, b2) else 0)
