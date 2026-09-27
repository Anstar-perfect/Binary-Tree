
from binarytree import *

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right  = Node(7)

print('Binary tree Structure:')
print(root)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value,end=" ")
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node:
        print(node.value,end = ' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value,end=' ')

print('\nIn order traversal:')
in_order_traversal(root)
print('\n')

print('Pre order traversal:')
pre_order_traversal(root)
print('\n')

print('Post order traversal:')
post_order_traversal(root)

