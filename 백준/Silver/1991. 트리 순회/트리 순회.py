class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end='')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end='')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end='')

if __name__ == '__main__':
    n = int(input())
    nodes = {}

    for _ in range(n):
        parent, left, right = input().split()
        if parent not in nodes:
            nodes[parent] = Node(parent)
        if left != '.' and left not in nodes:
            nodes[left] = Node(left)
        if right != '.' and right not in nodes:
            nodes[right] = Node(right)

        nodes[parent].left = nodes[left] if left != '.' else None
        nodes[parent].right = nodes[right] if right != '.' else None
    
    root = nodes['A']
    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)