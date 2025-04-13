import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
min_sum = float('inf')
result = []

for i in range(n - 2):
    start, end = i + 1, n - 1

    while start < end:
        total = arr[i] + arr[start] + arr[end]

        if abs(total) < min_sum:
            min_sum = abs(total)
            result = [arr[i], arr[start], arr[end]]

        if total < 0:
            start += 1
        elif total > 0:
            end -= 1
        else:
            print(arr[i], arr[start], arr[end])
            sys.exit(0)

print(*result)
