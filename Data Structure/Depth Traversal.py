def depth_first_traversal(node): 
 visited.append(node)
 for i in graph[node]: 
  if i not in visited: 
   depth_first_traversal(i)  
 return

graph={"A":["D","B"], "B":["A","E","C","F"],
"C": ["B","F"], "D": ["A","E"],
"E":["D","B"],"F":["B","C"]}

visited = []
depth_first_traversal("A")
print(visited)