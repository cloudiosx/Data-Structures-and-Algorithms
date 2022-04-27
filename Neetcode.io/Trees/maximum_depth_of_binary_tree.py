# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFT - Iterative
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        array = []

        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()
            
            if len(array) == level:
                array.append([node.val])
            else:
                array[level].append(node.val)

            if node.right:
                stack.append((node.right, level + 1))

            if node.left:
                stack.append((node.left, level + 1))

        return len(array)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])

        return res

# DFT - Recursive
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# BFT - Iterative
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        level += 1
        
    return level