class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# Iterative

# A --> B --> C --> D --> None
# current
def print_listIterative(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

# Recursive

# A --> B --> C --> D --> None
# head
def print_listRecursive(head):
    if head is None:
        return
    print(head.val)
    print_listRecursive(head.next)


print_listIterative(a)
print_listRecursive(a)

