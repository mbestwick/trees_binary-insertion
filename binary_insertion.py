"""
You are given a pointer to the root of a binary search tree and a value to be
inserted into the tree. Insert this value into its appropriate position in the
binary search tree and return the root of the updated binary tree. You just have
to complete the function.

"""


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(r, val):
    if not r:
        r = Node(val)
    elif val < r.data:
        r.left = insert(r.left, val)
    elif val > r.data:
        r.right = insert(r.right, val)
    return r
