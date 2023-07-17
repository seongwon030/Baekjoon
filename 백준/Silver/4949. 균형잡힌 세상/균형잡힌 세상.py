import sys

input = sys.stdin.readline

k = []

while True:
  s = input().rstrip()
  if s=='.':
    break
  else:
    for i in range(len(s)):
      if not k:
        if s[i]=='(' or s[i]=='[':
          k.append(s[i])
        elif s[i]==')' or s[i]==']':
          k.append(0)
          break
        else:
          continue
      else:
        if s[i]=='(' or s[i]=='[':
          k.append(s[i])
        elif s[i]==')':
          if k[-1]=='(':
            k.pop(-1)
          else:
            break
        elif s[i]==']':
          if k[-1]=='[':
            k.pop(-1)
          else:
            break
        else:
          continue
    if not k:
      print("yes")
    else:
      print("no")
    k.clear()