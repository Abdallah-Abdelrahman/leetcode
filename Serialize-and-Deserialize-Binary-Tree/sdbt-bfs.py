#!/usr/bin/env python3
'''Module define solution to Serialize and Deserialize Binary Tree'''

from collections import deque

class TreeNode(object):
    # TreeNode class for representing a node in a binary tree
    def __init__(self, x):
        self.val = x  # Node value
        self.left = None  # Left child
        self.right = None  # Right child

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        The method uses breadth-first search (BFS) to traverse the tree level by level.
        Null children are represented by '.' to maintain the tree structure in the string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""  # Return an empty string for an empty tree
        q = deque([root])  # Initialize a queue with the root
        s = ""  # Initialize the result string
        while q:
            node = q.popleft()  # Pop the first node in the queue
            if node:
                s += str(node.val) + ','  # Append the node value to the string
                q.append(node.left)  # Append left child to the queue
                q.append(node.right)  # Append right child to the queue
            else:
                s += '.,'  # Append '.' for null children
        return s

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        The method reconstructs the tree from the serialized string using BFS.
        It uses a queue to keep track of nodes to which children need to be added.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None  # Return None for an empty string
        nodes = data.split(",")[:-1]  # Split the string into nodes, excluding the last empty element
        root = TreeNode(int(nodes[0]))  # Create the root node
        q = deque([root])  # Initialize a queue with the root
        idx = 1  # Initialize index for the current node in the nodes list
        while q:
            node = q.popleft()  # Pop the first node in the queue
            if nodes[idx] != '.':
                left = TreeNode(int(nodes[idx]))  # Create left child if not '.'
                node.left = left  # Assign left child
                q.append(left)  # Append left child to the queue
            idx += 1
            if nodes[idx] != '.':
                right = TreeNode(int(nodes[idx]))  # Create right child if not '.'
                node.right = right  # Assign right child
                q.append(right)  # Append right child to the queue
            idx += 1
        return root