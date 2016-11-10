from kiwiland.directed_graph import DirectedGraph
from kiwiland.route_distance_calculator import RouteDistanceCalculator
from kiwiland.exception import InvalidRouteError
import pytest


class TestRouteDistanceCalculator:
    @pytest.fixture
    def route_spec(self):
        return [
            ("1. The distance of the route A-B-C.", 9),
            ("2. The distance of the route A-D.", 5),
            ("3. The distance of the route A-D-C.", 13),
            ("4. The distance of the route A-E-B-C-D.", 22),
        ]

    @pytest.fixture
    def graph(self):
        return DirectedGraph(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])

    def test_route_with_spec(self, route_spec, graph):
        for spec, expected_answer in iter(route_spec):
            calc = RouteDistanceCalculator(graph, spec)

        assert calc.route_distance == expected_answer

    def test_route_with_bad_spec(self, graph):
        with pytest.raises(InvalidRouteError) as bad_route_error:
            bad_route_spec = "5. The distance of the route A-E-D."
            calc = RouteDistanceCalculator(graph, bad_route_spec)
