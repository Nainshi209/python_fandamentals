# #WAP to implement singly linked list to perform operation delete a element.

# class Node:
#     def __init__(self,data):
#      self.data = data
#      self.next = None

# head = Node(10) 
# head.next = Node(20)
# head.next.next = Node(30)

# #delete element 20

# temp = head
# while temp.next.data !=20:
#    temp = temp.next
# temp.next = temp.next.next

# #display   
# while head:
#    print(head.data,end="->")
#    head = head.next



# import heapq
# heap =[]

#   #insert a element

# heapq.heappush(heap,30)  
# heapq.heappush(heap,10)  
# heapq.heappush(heap,20)  
# heapq.heappush(heap,5) 

# print(heap)
# #find peek element

# print("minimum element", heap[0])
# #delet minimum  element
# print("delete minimum element",heapq.heappop(heap))
# print("after deletion element",heap)


import heapq
heap = []
heapq.heappush(heap,-30)
heapq.heappush(heap,-20)
heapq.heappush(heap,-25)
heapq.heappush(heap,-10)
heapq.heappush(heap,-12)
heapq.heappush(heap,-21)
heapq.heappush(heap,-2)
print("max heap", [-x for x in heap])
deleted = heapq.heappop(heap)
print("deleted:",-deleted)
print("after deletion:",[-x for x in heap])


