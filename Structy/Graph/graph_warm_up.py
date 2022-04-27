# DFT - Iterative
def depth_first_print(graph, start):
	stack = [start]
	while len(stack) > 0:
		current = stack[-1]
		print(current)
		stack.pop()
		for neighbor in graph[current]:
			stack.append(neighbor)

# DFT - Recursive
def depth_first_print(graph, current):
	print(current)
	for neighbor in graph[current]:
		depth_first_print(graph, neighbor)

# BFT - Iterative
from collections import deque # double-ended queue
def breadth_first_print(graph, start):
	queue = deque([start])
	while len(queue) > 0:
		current = queue[0]
		print(current)
		queue.popleft()
		for neighbor in graph[current]:
			queue.append(neighbor)

graph = {
	"a": ["b", "c"],
	"b": ["d"],
	"c": ["e"],
	"d": ["f"],
	"e": [],
	"f": []
}

# print(depth_first_print(graph, "a"))
# print(breadth_first_print(graph, "a"))