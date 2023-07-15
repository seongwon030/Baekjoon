import sys

input = sys.stdin.readline

T = int(input())
k=[]
for i in range(T):
  n = input().rstrip() # 오른쪽 공백 제거를 위해 rstrip()
  if n[0] != '(' or n[-1] != ')': # 문자열의 처음이 (로 시작하지 않거나 마지막이 )로 끝나지 않으면 NO
    print("NO")
  else:
    for j in range(len(n)): 
      if n[j]=='(': 
        k.append(n[j])  # '(' 라면 리스트에 추가 
      else:
        if not k:     # 그게 아니면 k가 비어있을 때 ')'가 들어오면 안되므로 임의의 값인 0 넣고 종료 
          k.append(0)
          break
        else:
          k.pop()  # 비어 있지 않다면 리스트 마지막 요소를 제거 
    if not k:
      print("YES")  # 괄호의 수가 각각 같다면 리스트가 비어 있음 
    else:
      print("NO")
  k.clear()