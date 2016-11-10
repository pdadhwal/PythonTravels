from kiwiland.directed_graph import DirectedGraph
import pytest


class TestDirectedGraph:
    """Tests the DirectedGraph """

    @pytest.fixture
    def graph(self):
        return DirectedGraph(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])

    def test_can_create_graph(self, graph):
        assert graph.is_empty is not True

    def test_can_create_empty_graph(self):
        g = DirectedGraph()
        assert g.is_empty is True

    def test_can_iterate_over_edges(self, graph):
        for edge in graph.edges:
            pass

    def test_repr(self):
        g = DirectedGraph(['AB1'])
        assert repr(g) == 'DirectedGraph([Edge(AB1)])'
