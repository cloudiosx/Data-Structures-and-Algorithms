# Time: O(n) | Space: O(n) | n = # of nodes

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# DFT - Recursive
from statistics import mean

def level_averages(root):
  levels = []
  fill_levels(root, levels, 0)
  
  # avgs = []
  # for level in levels:
  #   avgs.append(mean(level))
  # return avgs

  return [mean(level) for level in levels]
    
def fill_levels(root, levels, level_num):
  if root is None:
    return
  
  if level_num == len(levels):
    levels.append([ root.val ])
  else:
    levels[level_num].append(root.val)
  
  fill_levels(root.left, levels, level_num + 1)
  fill_levels(root.right, levels, level_num + 1)

# BFT - Iterative
from collections import deque
def level_averages(root):
  if root is None:
    return []

  levels_averages = []

  levels = []
  queue = deque([(root, 0)])
 
  while queue:
    node, level = queue.popleft()

    if len(levels) == level:
      levels.append([node.val])
    else:
      levels[level].append(node.val)

    if node.left:
      queue.append((node.left, level + 1))

    if node.right:
      queue.append((node.right, level + 1))

  for subarray in levels:
    average = sum(subarray) / len(subarray)
    levels_averages.append(average)

  return levels_averages