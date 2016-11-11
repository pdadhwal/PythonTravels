class AdjacencyMatrix:
    def __init__(self, graph):
        self.__graph = graph
        self.__adjacency_matrix = {}
        self.__adjacency_matrix_built = False

    def get_adjacent_nodes(self, node):
        try:
            self.__build_adjacency_matrix()
            return self.__adjacency_matrix[node]
        except KeyError:
            return set()

    def __build_adjacency_matrix(self):
        if not self.__adjacency_matrix_built:
            for e in self.__graph.edges:
                points = (e.end, e.distance)
                if e.start not in self.__adjacency_matrix:
                    self.__adjacency_matrix[e.start] = set()

                set_of_node_and_distances = self.__adjacency_matrix[e.start]
                set_of_node_and_distances.add(points)

            self.__adjacency_matrix_built = True
