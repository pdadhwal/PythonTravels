from kiwiland.adjacency_matrix import AdjacencyMatrix
from kiwiland.exception import InvalidRouteError


class Route:
    def __init__(self, graph, path):
        self.__path = path
        self.__distance = 0

        adj_matrix = AdjacencyMatrix(graph)
        path_iter = iter(path.strip().split('-'))

        curr_node = next(path_iter)
        if len(curr_node.strip()) == 0:
            raise InvalidRouteError(path)

        try:
            while True:
                next_node = next(path_iter)
                adj_nodes = adj_matrix.get_adjacent_nodes(curr_node)

                if len(adj_nodes) == 0:
                    raise InvalidRouteError

                edges_to_next_node = [edge for edge in adj_nodes if edge._to == next_node]

                if len(edges_to_next_node) != 1:
                    message = "{0} not an adjacent node of {1} in {2}".format(curr_node, next_node, graph)
                    raise InvalidRouteError(message)
                else:
                    self.__distance += edges_to_next_node[0]._distance
                    pass

                curr_node = next_node
        except StopIteration:
            pass

    def __repr__(self):
        return "Route({0})".format(self.__path)

    @property
    def distance(self):
        return self.__distance
