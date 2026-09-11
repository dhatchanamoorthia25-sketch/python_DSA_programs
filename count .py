class Node:
   def__init__(self, data) ;
    self.data = data
    self.left = None
    self.right = None

    def count_nodes(self):
        if root is None:
            return 0
        return 1 + count_nodes(root.left) + count_nodes(root.right)

   root = Node(10)
   root.left = Node(20)
    root.right = Node(30)
   root.left.left = Node(40)


   print("total node:", count_nodes(root))
    