from kiwiland.exceptions import InvalidRouteError


class Route:
    def __init__(self, graph, path):
        self.__path = path
        self.__distance = 0

        path_iter = iter(path.strip().split('-'))

        curr_node = next(path_iter)
        if len(curr_node.strip()) == 0:
            raise InvalidRouteError(path)

        try:
            while True:
                next_node = next(path_iter)
                adj_nodes = graph.get_adjacent_nodes(curr_node)

                if len(adj_nodes) == 0:
                    raise InvalidRouteError

                distances = [distance for node, distance in adj_nodes if node == next_node]

                if len(distances) == 1:
                    self.__distance += distances[0]
                else:
                    message = "{0} not an adjacent node of {1} in {2}".format(curr_node, next_node, graph)
                    raise InvalidRouteError(message)

                curr_node = next_node
        except StopIteration:
            pass

    def __repr__(self):
        return "Route({0})".format(self.__path)

    @property
    def distance(self):
        return self.__distance
