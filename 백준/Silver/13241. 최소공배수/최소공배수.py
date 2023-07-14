a,b = map(int,input().split())
def gcd(a,b):
  while b>0:
    a,b = b, a%b
  return a

def lcm(a,b):
  result = (a*b) // gcd(a,b)
  return result

print(lcm(a,b))