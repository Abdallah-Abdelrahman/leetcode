#!/usr/bin/env python3
'''Module define solution to Serialize and Deserialize Binary Tree'''

class TreeNode(object):
    # TreeNode class for representing a node in a binary tree
    def __init__(self, x):
        self.val = x  # Node value
        self.left = None  # Left child
        self.right = None  # Right child

class Codec:
    # Codec class for serialization and deserialization of a binary tree

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        Uses pre-order traversal to serialize the tree, using '.' to represent null nodes
        and '|' as a separator between node values.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            # Helper function for recursive tree traversal
            if not node:
                return ".|"  # Representing null node
            # Serialize current node value and recursively serialize left and right children
            return str(node.val) + '|' + helper(node.left) + helper(node.right)
        return helper(root)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        Reconstructs the tree from the serialized string by splitting the string
        on '|' and using a recursive helper function to build nodes.
        
        :type data: str
        :rtype: TreeNode
        """
        vs = data.split("|")  # Split serialized string into values
        def helper(idx):
            # Helper function to recursively construct the tree
            val = vs[idx]
            if val == '.':
                return None, idx + 1  # Return None for null node and move to next index
            node = TreeNode(int(val))  # Create node with current value
            node.left, idx = helper(idx + 1)  # Recursively construct left subtree
            node.right, idx = helper(idx + 1)  # Recursively construct right subtree
            return node, idx
        node, _ = helper(0)  # Start reconstruction from first value
        return node