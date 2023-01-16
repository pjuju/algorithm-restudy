N = int(input())
left_node = [0] * (N+1)
right_node = [0] * (N+1)

def func(x):
    if x == '.':
        return 0
    else:
        return ord(x) - ord('A') + 1

def preorder(x):
    if x == 0:
        return
    print(chr(x+ord('A')-1), end='')
    preorder(left_node[x])
    preorder(right_node[x])

def inorder(x):
    if x == 0:
        return
    inorder(left_node[x])
    print(chr(x+ord('A')-1), end='')
    inorder(right_node[x])

def postorder(x):
    if x == 0:
        return
    postorder(left_node[x])
    postorder(right_node[x])
    print(chr(x+ord('A')-1), end='')

for _ in range(N):
    N, L, R = map(func,input().split())
    left_node[N] = L
    right_node[N] = R

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()
#
