import pytest
from kiwiland.directed_graph import DirectedGraph
from kiwiland.dfs import dfs_paths


class TestDFSPaths:
    @pytest.fixture
    def graph(self):
        return DirectedGraph(['AB1', 'AC1', 'BD1', 'CD1'])

    def test_dfs_path(self, graph):
        paths = sorted(list(dfs_paths(graph, 'A', 'D')))

        assert len(paths) == 2
        assert paths == [['A', 'B', 'D'], ['A', 'C', 'D']]

    def test_dfs_one_only(self, graph):
        paths = list(dfs_paths(graph, 'A', 'B'))

        assert len(paths) == 1
        assert paths == [['A', 'B']]

    def test_iterate_all_paths(self, graph):
        g = DirectedGraph(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])
        paths = dfs_paths(graph, 'A', 'E')
        for path in paths:
            print(path)

        pass
