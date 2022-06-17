# 문제 주소 : https://www.acmicpc.net/problem/1991

N = int(input())
tree = [ [0, 0]  for _ in range(N) ]
for i in range(N):
    root, left, right = map(lambda x: ord(x)-65, input().split())
    tree[root][0] = left
    tree[root][1] = right

def preorder(root):
    result = []
    def recur(parent):   
        if parent < 0:
            return
        
        result.append( chr(parent+65) )
        recur(tree[parent][0])
        recur(tree[parent][1])
    
    recur(root)
    return ''.join(result)

def inorder(root):
    result = []
    def recur(parent):   
        if parent < 0:
            return
        
        recur(tree[parent][0])
        result.append( chr(parent+65) )
        recur(tree[parent][1])
    
    recur(root)
    return ''.join(result)

def postorder(root):
    result = []
    def recur(parent):   
        if parent < 0:
            return
        
        recur(tree[parent][0])
        recur(tree[parent][1])
        result.append( chr(parent+65) )
    
    recur(root)
    return ''.join(result)

print( preorder(0) )
print( inorder(0) )
print( postorder(0) )