class AdjacencyMatrix:

    def __init__(self, graph):
        self.__graph = graph
        self.__adjacency_matrix = {'': []}
        self.__adjacency_matrix_built = False

    def get_adjacent_nodes(self, node):
        try:
            self.__build_adjacency_matrix()
            return self.__adjacency_matrix[node]
        except KeyError:
            return list([])

    def __build_adjacency_matrix(self):
        if not self.__adjacency_matrix_built:
            for e in self.__graph.edges:
                if self.__adjacency_matrix.__contains__(e._from):
                    self.__adjacency_matrix[e._from].append(e)
                else:
                    self.__adjacency_matrix[e._from] = [e]
            self.__adjacency_matrix_built = True
