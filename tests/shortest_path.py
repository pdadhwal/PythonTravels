import pytest
from kiwiland.directed_graph import DirectedGraph
from kiwiland.shortest_path import shortest_path


class TestShortestPath:

    @pytest.fixture
    def graph(self):
        return DirectedGraph(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])

    def test_shortest_path(self, graph):
        path = shortest_path(graph, 'A', 'C')

        assert path.distance == 9

    def test_shortest_path_bad_route(self, graph):
        path = shortest_path(graph, 'E', 'A')

        assert path is None
