class Node:

  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None
    self.height = 0


class BST:

  def __init__(self):
    self.root = None

  def height(self, node):
    if node is None:
      return -1
    return node.height

  def insert(self, node, data):
    if node is None:
      return Node(data)

    if data < node.data:
      node.left = self.insert(node.left, data)
    elif data > node.data:
      node.right = self.insert(node.right, data)
    else:
      # Ignore duplicates
      return node

    node.height = max(self.height(node.left), self.height(node.right)) + 1
    balance = self.balanced_check(node)
    print(f"Balance at {node.data} is balance {balance}")
    return node

  def insert_data(self, data):
    self.root = self.insert(self.root, data)

  def balanced_check(self, node):
    if node is None:
        return True

    # left_height = 
    # right_height = 

    return (abs(self.height(node.left) - self.height(node.right)) <= 1) and \
           self.balanced_check(node.left) and \
           self.balanced_check(node.right)

    

  def inorder(self, node):
    if node is None:
      return node
    self.inorder(node.left)
    print(f"Node data is {node.data} and height is {node.height}")
    self.inorder(node.right)


bst = BST()
bst.insert_data(5)
bst.insert_data(1)
bst.insert_data(2)
bst.insert_data(6)

bst.inorder(bst.root)
