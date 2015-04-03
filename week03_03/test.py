graph = {
    "1": ["2", "3", "5", "10"],
    "2": ["4", "1"],
    "3": ["1", "6"],
    "4": ["2", "5", "6"],
    "5": ["4", "1"],
    "6": ["3", "4", "7"],
    "7": ["6", "8"],
    "8": ["7", "9"],
    "9": ["8", "10"],
    "10": ["9", "1"]
}

#bfc 
def bfs(graph, start, end):
    visited = set()
    queue = []
    # Path to x = y if we go to x through y
    pathTo = {}

    queue.append(start)
    visited.add(start)
    pathTo[start] = None
    found = False
    path_length = 0

    while len(queue) != 0:
        current_node = queue.pop(0) # vadim ot opashkata neposeteni 

    if current_node == end:
        #return True
        found = True

    for neighbour in graph[current_node]:
        if neighbour not in visited:
            path_to[neighbour] = current_node
            visited.add(neighbour)
            queue.append(neighbour)

    if found:
        while path_to[end] is not None:
            path_length += 1
            end = path_to[end]

print(bfs(graph, "1", "7"))