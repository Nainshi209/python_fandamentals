# class node:
#     def __init__(self,data):
#        self.data= data    #store thr value
#        self.next= None     #store the reference to the next node

#        class LinkedList:
#            def __init__():
#               self.head= None     #keeps track of the start of  the list



#         #creat a node
# node1 = node(25)
# node2 = node(35)
# node3 = node(45)
# node4 = node(55)


#         #link the each of node
# node1.next = node2  #Node1 to point Node2 address
# node2.next = node3
# node3.next = node4
#         #set the head node
# head = node1

#        #make a temporary pointer
        
# current = head

# while current is not None:
             
#     print(current.data,end=" -> ")
#     current = current.next #move next node
# print("None")  







# class node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None


#         #Create node
# node1 = node(34)
# node2 = node(45)
# node3 = node(54)

# #connect nodes
# node1.next = node2
# node2.prev = node1

# node2.next = node3
# node3.prev = node2

# #insert a element in particular between 45 and 54 insert element 25
# #create a new node
# new_node =node(25)

# #step1:
# new_node.next = node2.next

# #step2: connect 25 to 45
# new_node.prev = node2

# #step3: connect 45 to 25
# node2.next.prev = new_node

# #step4: 
# node2.next = new_node


# #insert a element in particular between 34 and 45 insert element 15
# #create a new node
# new_node = node(15)

# # step1: 
# new_node.next = node1.next

# #step2: connect 15 to 34
# new_node.prev = node1

# #step3: connect 34 to 15
# node1.next.prev = new_node

# #step4: 
# node1.next = new_node  



# #forward traversal
# current = node1
# while current is not None:
#     print(current.data,end=" -> ")
#     current = current.next
# print("None")





class node:
    def __init__(self,data):
        self.data= data
        self.prev = None
        self.next = None
#first create a node
node1= node(10)
node2= node(20)
node3= node(30)
node4= node(40)

# connect each of node

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

#delete node3 (25)
# connect node 20 to 30
node3.prev.next = node3.next

#again 3o back to connect
node3.next.prev = node3.prev







#forword traversal
current = node1
while current is not None:
    print(current.data,end=" -> ")
    current = current.next
print("None")