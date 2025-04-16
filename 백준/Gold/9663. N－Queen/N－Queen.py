def queens(level):
    global count
    if level == n:
        count += 1
        return
    
    for i in range(n):
        cols[level] = i
        if is_promising(level):
            queens(level + 1)

def is_promising(level):
    for i in range(level):
        if (cols[i] == cols[level] or abs(cols[i] - cols[level]) - abs(level - i) == 0):
            return False
    return True


n = int(input())
cols = [0] * n
count = 0

queens(0)
print(count)