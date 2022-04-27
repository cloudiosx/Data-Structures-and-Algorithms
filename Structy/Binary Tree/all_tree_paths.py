# Time: ~O(n) | Space: ~O(n) | n = # of nodes

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# DFT - Recursive - Not optimized
def all_tree_paths(root):
  if root is None:
    return []
  
  if root.left is None and root.right is None:
    return [ [root.val] ]
  
  paths = []
  
  left_sub_paths = all_tree_paths(root.left)
  for sub_path in left_sub_paths:
    paths.append([ root.val, *sub_path ])
    
  right_sub_paths = all_tree_paths(root.right)
  for sub_path in right_sub_paths:
    paths.append([ root.val, *sub_path ])
    
  return paths

# DFT - Recursive - Optimized
def all_tree_paths(root):
  result = _all_tree_paths(root)

  if result is None:
    return None
  else:
    for ele in result:
      ele.insert(0, ele.pop())
    return result

def _all_tree_paths(root):
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [[root.val]]

  paths = []

  left_sub_paths = all_tree_paths(root.left)
  for sub_paths in left_sub_paths:
    sub_paths.append(root.val)
    paths.append(sub_paths)

  right_sub_paths = all_tree_paths(root.right)
  for sub_paths in right_sub_paths:
    sub_paths.append(root.val)
    paths.append(sub_paths)


  return paths
