class Node:

  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None
    self.height = 0


class AVL:

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
        print("Inserting ", data)
        node.left = self.insert(node.left, data)
    elif data > node.data:
        node.right = self.insert(node.right, data)
    else:
        # Ignore duplicates
        return node

    node.height = max(self.height(node.left), self.height(node.right)) + 1
    return self.rotate(node)


  def rotate(self, node):
      if self.height(node.left) - self.height(node.right) > 1: 
        #   Left heavy
          if self.height(node.left.left) - self.height(node.left.right) > 0:
            #   Left left case
              return self.rightRotate(node)
          if self.height(node.left.left) - self.height(node.left.right) < 0:
            #   Left right case
              node.left = self.leftRotate(node.left)
              return self.rightRotate(node)
          
      if self.height(node.left) - self.height(node.right) < -1: 
        #   Right heavy
          if self.height(node.right.left) - self.height(node.right.right) < 0:
            #   right right case
              return self.leftRotate(node)
          if self.height(node.right.left) - self.height(node.right.right) > 0:
            # Right left case
            node.right = self.rightRotate(node.right)  
            return self.leftRotate(node)

      return node
  
  def rightRotate(self, r):
      p = r.left
      q = p.right
      
      p.right = r
      r.left = q
      
      p.height = max(self.height(p.left), self.height(p.right)) + 1
      r.height = max(self.height(r.left), self.height(r.right)) + 1
      
      return p
  
  def leftRotate(self, r):
      p = r.right
      q = p.left
      
      p.left = r
      r.right = q
      
      p.height = max(self.height(p.left), self.height(p.right)) + 1
      r.height = max(self.height(r.left), self.height(r.right)) + 1
      
      return p
      
      
      

  def insert_data(self, data):
    self.root = self.insert(self.root, data)

  def balanced_check(self, node):
    if node is None:
        return True


    return (abs(self.height(node.left) - self.height(node.right)) <= 1) and \
           self.balanced_check(node.left) and \
           self.balanced_check(node.right)

    

  def inorder(self, node):
    if node is None:
      return node
    self.inorder(node.left)
    print(f"{node.data}", end =" ")
    self.inorder(node.right)

  def is_avl(self):
        return self._is_avl(self.root)

  def _is_avl(self, node):
        if node is None:
            return True
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return self._is_avl(node.left) and self._is_avl(node.right)


avl = AVL()
avl.insert_data(5)
avl.insert_data(2)
avl.insert_data(1)
avl.insert_data(0)

avl.inorder(avl.root)

print(avl.is_avl())

