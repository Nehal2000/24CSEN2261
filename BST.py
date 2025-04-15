class Node:
    def _init_(self, key):
        self.left = self.right = None
        self.value = key

class BST:
    def _init_(self):
        self.root = None

    # Insert a new node
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if not node.left:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if not node.right:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    # Inorder traversal
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        return self._inorder(node.left) + [node.value] + self._inorder(node.right) if node else []

# Example usage:
bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(15)

# Inorder traversal (sorted order)
print(bst.inorder())
