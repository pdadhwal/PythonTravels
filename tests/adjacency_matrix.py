from kiwiland.adjacency_matrix import AdjacencyMatrix
from kiwiland.directed_graph import DirectedGraph
import pytest


class TestAdjacencyMatrix:
    @pytest.fixture
    def graph(self):
        return DirectedGraph(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])

    @pytest.fixture
    def adjmatrix(self, graph):
        return AdjacencyMatrix(graph)

    def test_can_retrieve_valid_adjacent_nodes(self, adjmatrix):
        adjacent_nodes = adjmatrix.get_adjacent_nodes('A')
        assert len(adjacent_nodes) == 3

    def test_check_with_invalid_adjacent_nodes(self, adjmatrix):
        adjacent_nodes = adjmatrix.get_adjacent_nodes('Z')
        assert len(adjacent_nodes) == 0
