class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def create(node, arr, s, ind):
    while ind < len(arr):
        if arr[ind] not in s:
            node1 = Node(arr[ind])
            s.add(arr[ind])
            node.children.append(node1)
            ind += 1
            if ind >= len(arr):
                break
            if arr[ind] != node1.val:
                create(node1, arr, s, ind)
            else:
                ind += 1
        else:
            ind += 1

def dfs(node, a, b, c):
    global ans
    if l[node.val - 1] == 'A':
        if abs(a - c) != 1:
            ans[node.val - 1] = abs(a - c) - 1
        for i in node.children:
            dfs(i, a + 1, b, c + 1)
    else:
        if abs(b - c) != 1:
            ans[node.val - 1] = abs(b - c) - 1
        for i in node.children:
            dfs(i, a, b + 1, c + 1)

n = int(input())

l = list(input().split())
ans = [0] * n

arr = list(map(int, input().split()))

node = Node(arr[0])
s = set()
s.add(arr[0])

create(node, arr, s, 1)

for i in node.children:
    dfs(i, 0, 0, 1)

print(*ans)
