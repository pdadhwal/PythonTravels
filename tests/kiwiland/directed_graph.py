import pytest

from kiwiland.directed_graph import DirectedGraph


class TestDirectedGraph:
    """Tests the DirectedGraph """

    @pytest.fixture
    def graph(self):
        return DirectedGraph(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])

    def test_create_graph(self, graph):
        assert graph.is_empty is not True

    def test_create_empty_graph(self):
        g = DirectedGraph()
        assert g.is_empty is True

    def test_iterate_over_edges(self, graph):
        for edge in graph.edges:
            pass

    def test_repr(self):
        g = DirectedGraph(['AB1'])
        assert repr(g) == 'DirectedGraph([Edge(AB1)])'

    def test_nodes(self, graph):
        assert graph.nodes == {'A', 'B', 'C', 'D', 'E'}

    def test_check_with_invalid_adjacent_nodes(self, graph):
        adjacent_nodes = graph.get_adjacent_nodes('Z')
        assert len(adjacent_nodes) == 0

    def test_can_retrieve_valid_adjacent_nodes(self, graph):
        adjacent_nodes = list(sorted(graph.get_adjacent_nodes('A')))
        assert len(adjacent_nodes) == 3

        t1 = adjacent_nodes[0]
        condition1 = t1[0] == 'B' and t1[1] == 5

        t2 = adjacent_nodes[1]
        condition2 = t2[0] == 'D' and t2[1] == 5

        t3 = adjacent_nodes[2]
        condition3 = t3[0] == 'E' and t3[1] == 7

        assert condition1 and condition2 and condition3
