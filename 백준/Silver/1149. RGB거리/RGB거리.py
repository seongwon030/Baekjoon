n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]                    
k = [[0] *3 for _ in range(n+1)]

for i in range(1,n+1):
    k[i][0] = min(k[i-1][1],k[i-1][2])+d[i-1][0]
    k[i][1] = min(k[i-1][0],k[i-1][2])+d[i-1][1]
    k[i][2] = min(k[i-1][0],k[i-1][1])+d[i-1][2]
print(min(k[n][0], k[n][1], k[n][2]))