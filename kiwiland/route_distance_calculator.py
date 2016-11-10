from kiwiland.route import Route
import re


class RouteDistanceCalculator:
    def __init__(self, graph, spec):
        self.__pattern = r'^([\d+]+)\.\s*The distance of the route (([A-Z]+-*)+)\.'
        m = re.match(self.__pattern, spec)
        self.__testid = m.group(1)
        self.__route = Route(graph, m.group(2))

    @property
    def route_distance(self):
        return self.__route.distance
