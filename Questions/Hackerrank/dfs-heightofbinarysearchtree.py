def getBinarySearchTreeHeight(values, leftChild, rightChild):
    if len(values) == 0:
        return 0
    root = 0
    def dfs(node):
        if node == -1:
            return 0
        left_h = dfs(leftChild[node])
        right_h = dfs(rightChild[node])
        return 1 + max(left_h , right_h)
    return dfs(root)
def getBinarySearchTreeHeight(values, leftChild, rightChild):
    if len(values) == 0:
        return 0
    n = len(values)
    isChild = [False] * n
    
    for i in range(n):
        if leftChild[i] != -1:
            isChild[leftChild[i]] = True
        if rightChild[i] != -1:
            isChild[rightChild[i]] = True
    root = 0
    for i in range(n):
        if not isChild[i]:
            root = i
            break
    def dfs(node):
        if node == -1:
            return 0
        left_h = dfs(leftChild[node])
        right_h = dfs(rightChild[node])
        
        return 1 + max(left_h , right_h)
    
    return dfs(root)
