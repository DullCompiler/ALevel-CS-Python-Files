def breadth_first_traversal(node):
 queue = []
 queue.append(node)
 visited.append(node)
 
 while len(queue) > 0:
  node = queue.pop(0)
  print (node, end = " ")                
  for i in graph[node]: 
   if i not in visited:               
    queue.append(i)
    visited.append(i)

graph={'A':['D','B'], 'B':['A','E','C','F'], 'C': ['B','F'],'D': ['A','E'], 'E':['D','B'],'F':['B','C']}

visited = []
breadth_first_traversal("A")