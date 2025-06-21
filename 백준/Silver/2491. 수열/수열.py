def longest_monotonic_subarray(arr):
    inc_len = dec_len = max_len = 1

    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            inc_len += 1
        else:
            inc_len = 1

        if arr[i] <= arr[i-1]:
            dec_len += 1
        else:
            dec_len = 1

        max_len = max(max_len, inc_len, dec_len)

    return max_len

n = int(input())
A = list(map(int, input().split()))

print(longest_monotonic_subarray(A))