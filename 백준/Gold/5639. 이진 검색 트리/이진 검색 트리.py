import sys
sys.setrecursionlimit(10**6)

# 전위 순회 결과로 트리 복구
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 1. 첫번째 값은 루트
# 2. 그 뒤로 루트보다 작은 값들 -> 왼쪽 서브트리
# 3. 큰 값들 오른쪽 서브트리
# 4. 위 구조대로 재귀적으로 트리 만들고
# 5. 후위 순회로 출력

def bst_from_preorder(preorder):
    # bounds: 현재 노드가 들어갈 수 있는 값의 범위
    def helper(bounds):
        nonlocal index
        if index >= len(preorder) or not(bounds[0] < preorder[index] < bounds[1]):
            return None
        root_val = preorder[index]
        index += 1
        node = Node(root_val)
        node.left = helper((bounds[0], root_val))
        node.right = helper((root_val, bounds[1]))
        return node

    index = 0
    return helper((float('-inf'), float('inf')))

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end='\n')

if __name__ == '__main__':
    preorder = []
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            preorder.append(n)
        except:
            break


    bst = bst_from_preorder(preorder)
    postorder(bst)

