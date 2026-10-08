class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
     #create a function in_order traversal
def pre_order(root):
        
        if root is None:

            return
    #step: visit left subtree
        print(root.data, end= " ")

    #step2: visit right
        pre_order(root.left)

    #step3: visit right subtree
        pre_order(root.right)

#create a tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#function calling or driver code calling
pre_order(root)