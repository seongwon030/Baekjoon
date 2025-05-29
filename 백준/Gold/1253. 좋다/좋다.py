import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

start, end = 0, n-1
count = 0

for i in range(n-1,-1,-1):
    good_number = arr[i]
    start, end = 0, n-1
    while start < end:
        if start == i:
            start += 1
        elif end == i:
            end -= 1
        elif arr[start] + arr[end] < good_number:
            start += 1
        elif arr[start] + arr[end] > good_number:
            end -=1
        else:
            count += 1
            break

print(count)