# # import deque (double ended queue ) from the collections module.
# from collections import deque

# #create the graph using an adjacency list 
# #each key is a vertex , and its value is a list of connected vertices
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'E'],
#     'D': ['B', 'E'],
#     'E': ['C', 'D'],
# }
# def dfs(graph, start):
#     visited =set()
#     stack = [start]

#     while stack:
#       vertex = stack.pop()

#       if vertex not in visited:
#          visited.add(vertex)
#          print(vertex, end = " ")

#          for neighbor in  reversed(graph[vertex]):
#             if neighbor not in visited:
#                stack.append(neighbor)
       
# dfs(graph, 'A')





from collections import deque
graph = {
    '1': ['6', '7', '5'],
    '6': ['10'],
    '7': ['9', '3'],
    '5': ['9', '4'],
    '10': ['8'],
    '3': ['8'],
    '9': ['2'],
    '4': ['2'],
    '8': [ ],
    '2': [ ],
}
def dfs(graph, start):
    visited =set()
    stack = [start]

    while stack:
      vertex = stack.pop()

      if vertex not in visited:
         visited.add(vertex)
         print(vertex, end = " ")

         for neighbor in  reversed(graph[vertex]):
            if neighbor not in visited:
               stack.append(neighbor)
       
dfs(graph, '1')