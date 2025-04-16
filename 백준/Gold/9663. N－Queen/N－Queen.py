def queens(level):
    global count
    if level == N:
        count += 1
        return
    else:
        for i in range(N):
            cols[level] = i
            if promising(level):
                queens(level + 1)

def promising(level):
    for i in range(level):
        if (cols[i] == cols[level]) or abs(cols[i] - cols[level]) == abs(level - i):
            return False
    return True


N = int(input())
count = 0
cols = [0] * N


queens(0)
print(count)