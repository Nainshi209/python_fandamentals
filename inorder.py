class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
     #create a function in_order traversal
def in_order(root):
        
        if root is None:

            return
    #step: visit left subtree
        in_order(root.left)

    #step2: visit right
        print(root.data, end= " ")

    #step3: visit right subtree
        in_order(root.right)

#create a tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#function calling or driver code calling
in_order(root)