from kiwiland.edge import Edge


class DirectedGraph:
    """ Represents a directed graph of nodes and edges """

    def __init__(self, edges=None):
        """ Creates a DirectedGraph """
        if edges is not None:
            self.__edges = DirectedGraph.__get_edges(edges)
        else:
            self.__edges = set()

        nodes = []
        for edge in self.__edges:
            nodes.append(edge.start)
            nodes.append(edge.end)

        self.__nodes = set(nodes)

        self.__adjacency_matrix = {}
        for e in self.__edges:
            points = (e.end, e.distance)
            if e.start not in self.__adjacency_matrix:
                self.__adjacency_matrix[e.start] = set()

            set_of_node_and_distances = self.__adjacency_matrix[e.start]
            set_of_node_and_distances.add(points)

    def get_adjacent_nodes(self, node):
        try:
            return self.__adjacency_matrix[node]
        except KeyError:
            return set()

    def __getitem__(self, item):
        try:
            return {x for x, distance in self.__adjacency_matrix[item]}
        except KeyError:
            return set()

    @staticmethod
    def __get_edges(edges):
        """Builds a set of edges by iterating over the input"""
        returned_edges = set()
        for edge in edges:
            returned_edges.add(Edge(edge))
        return sorted(returned_edges)

    @property
    def is_empty(self):
        """ Return true if the graph is empty"""
        return len(self.__edges) == 0

    @property
    def edges(self):
        """ Return edges in the DirectedGraph"""
        return self.__edges

    @property
    def nodes(self):
        return self.__nodes

    def __repr__(self):
        return "DirectedGraph({0})".format(self.__edges)
