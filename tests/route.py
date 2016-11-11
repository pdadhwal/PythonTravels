from kiwiland.directed_graph import DirectedGraph
from kiwiland.exceptions import InvalidRouteError
from kiwiland.route import Route

import pytest


class TestRoute:
    @pytest.fixture
    def graph(self):
        return DirectedGraph(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])

    def test_cannot_create_empty_route(self):
        with pytest.raises(InvalidRouteError):
            route = Route(DirectedGraph(), '')

    def test_bad_route_raises_invalid_route_error(self, graph):
        with pytest.raises(InvalidRouteError):
            route = Route(graph, 'A-Z-D')

    def test_bad_route_raises_invalid_route_error_when_no_nodes_are_in(self, graph):
        with pytest.raises(InvalidRouteError):
            route = Route(graph, 'X-Y-Z')

    def test_can_create_good_route(self, graph):
        route = Route(graph, 'A-B-C-D')

    def test_repr(self, graph):
        route = Route(graph, 'A-B-C-D')
        assert repr(route) == "Route(A-B-C-D)"

    def test_route_distance(self, graph):
        route = Route(graph, 'A-B-C-D')
        assert route.distance == 17
