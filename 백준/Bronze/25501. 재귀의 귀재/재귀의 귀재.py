cnt = 0
def recursion(s, l, r):
    global cnt
    if l >= r: 
      cnt += 1
      return 1
    elif s[l] != s[r]: 
      cnt += 1
      return 0
    else: 
      cnt += 1
      return recursion(s, l+1, r-1)
    

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
for i in range(T):
  k = input()
  print(isPalindrome(k), cnt)
  cnt = 0