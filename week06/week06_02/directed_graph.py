class DirectedGraph:

    def __init__(self):
        self.vertices = {}

    def add_edge(self, node_a, node_b):
        if node_a not in self.vertices:
            self.vertices[node_a] = [node_b]
        else:
            self.vertices[node_a].append(node_b)

        if node_b not in self.vertices:
            self.vertices[node_b] = []

    def get_neihbours(self, node):
        if node not in self.vertices:
            print("Node not in the graph")
            return

        return self.vertices[node]

    def path_between(self, node_a, node_b):
        queue = [node_a]
        visited = set(node_a)

        while queue:
            current_vertice = queue.pop(0)
            if current_vertice == node_b:
                return True

            for vertex_neighbour in self.vertices[current_vertice]:
                if vertex_neighbour not in visited:
                    queue.append(vertex_neighbour)
                    visited.add(vertex_neighbour)

        return False

    def print_graph(self):
        print(self.vertices)



