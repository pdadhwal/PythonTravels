import re

from kiwiland.exceptions import InvalidRouteSpecError


class DistanceRouteSpec:
    def __init__(self, route_spec):
        self.__pattern = r'^([\d+]+)\.\s*The distance of the route (([A-Z]+-*)+)\.'
        m = re.match(self.__pattern, route_spec)

        if m:
            self.__testid = m.group(1)
            self.__route = m.group(2)
        else:
            raise InvalidRouteSpecError(route_spec)

    @property
    def testid(self):
        return self.__testid

    @property
    def route(self):
        return self.__route


class RoutesBetweenNodesWithMaxStopsSpec:
    def __init__(self, route_spec):
        pattern = r'^([\d+]+)\.\s*The number of trips starting at ([A-Z]) and ending at ([A-Z]) with a maximum ' \
                  r'of ([\d]) stops.'
        m = re.match(pattern, route_spec)

        if m:
            self.__testid = m.group(1)
            self.__start = m.group(2)
            self.__end = m.group(3)
            self.__num_stops = int(m.group(4))
        else:
            raise InvalidRouteSpecError(route_spec)

    @property
    def testid(self):
        return self.__testid

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    @property
    def num_stops(self):
        return self.__num_stops
