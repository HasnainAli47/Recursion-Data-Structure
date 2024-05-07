class Node:

  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None


class BST:

  def __init__(self):
    self.root = None

  def AskUser(self):
    print("Do you want to insert new node?")
    print("Enter 1 for yes and 0 for no")
    choice = int(input())
    return choice

  def insert(self, node, data):
    if self.root is None:
      self.root = Node(data)
      if self.AskUser() == 1:
        self.insert(self.root, int(input("Enter the data: ")))
    elif data < int(node.data):
      if node.left is None:
        node.left = Node(data)
        # Ask user if want to insert new node
        if self.AskUser() == 1:
          self.insert(self.root, int(input("Enter the data: ")))
      else:
        self.insert(node.left, data)
    else:
      if node.right is None:
        node.right = Node(data)
        # Ask user if want to insert new node
        if self.AskUser() == 1:
          self.insert(self.root, int(input("Enter the data: ")))
      else:
        self.insert(node.right, data)

  def inorder(self, node):
    if node is None:
      return
    self.inorder(node.left)
    print(node.data, end=" ")
    self.inorder(node.right)


bst = BST()
bst.insert(bst.root, input("Enter data for the root node: "))
bst.inorder(bst.root)
