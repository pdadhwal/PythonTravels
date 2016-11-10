from kiwiland.route import Route


class RouteDistanceCalculator:
    def __init__(self, graph, distance_route_spec):
        self.__route = Route(graph, distance_route_spec.route)

    @property
    def route_distance(self):
        return self.__route.distance
