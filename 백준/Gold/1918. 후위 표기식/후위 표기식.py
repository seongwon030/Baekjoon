opr = list(input())

ans = []
alp = ''

for k in opr:
  if k.isalpha():
    alp+=k
  else:
    if k=='(':
      ans.append(k)
    elif k == '*' or k == '/':
      while ans and (ans[-1] == '*' or ans[-1] == '/'):
        alp+=ans.pop()
      ans.append(k)
    elif k == '+' or k == '-':
      while ans and ans[-1] != '(':
        alp+=ans.pop()
      ans.append(k)
    elif k == ')':
      while ans and ans[-1] != '(':
        alp+=ans.pop()
      ans.pop()

while ans:
  alp+=ans.pop()

print(alp)