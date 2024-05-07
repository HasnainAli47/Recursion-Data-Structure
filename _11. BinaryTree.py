# make the node for the tree to be inserted
class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


# Make a BinaryTree class
class BinaryTree:

  def __init__(self):
    self.root = None

  # Make the root of the tree
  def insert_root(self, data):
    if self.root is None:
      self.root = Node(data)
      self.insert(self.root)
      self.inorder(self.root)  #print tree in inorder
    else:
      print("Root already exists")

  def insert(self, node):
    # Ask use that if want to put the left node of the root
    print(f"Do you want to put the left node of the {node.data}?")
    print("Enter 1 for yes and 0 for no")
    choice = int(input())
    if choice == 1:
      node.left = Node(int(input("Enter the data: ")))
      self.insert(node.left)
    # Now ask if want to put the right node of the root
    print(f"Do you want to put the right node of the {node.data}?")
    print("Enter 1 for yes and 0 for no")
    choice = int(input())
    if choice == 1:
      node.right = Node(int(input("Enter the data: ")))
      self.insert(node.right)

  def inorder(self, node):
    if node is None:
      return
    self.inorder(node.left)
    print(node.data, end=" ")
    self.inorder(node.right)


binaryTree = BinaryTree()
binaryTree.insert_root(int(input("Enter the root node data: ")))
