from kiwiland.edge import Edge
import pytest


class TestEdge:
    """Tests the Edge """

    @pytest.fixture
    def edge(self):
        return Edge('AB5')

    def test_can_create_edge(self, edge):
        pass

    def test_cannot_create_empty_edge(self):
        with pytest.raises(TypeError):
            e = Edge()

    def test_cannot_create_bad_edge(self):
        with pytest.raises(ValueError) as valError:
            e = Edge('AB')
        assert 'Edge must have atleast 3 elements. e.g AB4' in str(valError)

    def test_retrieve_from_to_and_distance(self, edge):
        assert edge._from == 'A'
        assert edge._to == 'B'
        assert edge._distance == 5

    def test_edge_from_to_cannot_be_same_node(self):
        with pytest.raises(ValueError) as valError:
            e = Edge('AA1')
        assert 'Edge cannot start and end at the same node' in str(valError)

    def test_edges_are_equal(self):
        e1 = Edge('AB1')
        e2 = Edge('AB1')

        assert e1 == e2

    def test_edges_are_equal(self):
        e1 = Edge('AB1')
        assert e1 == e1

    def test_edges_not_equal(self):
        e1 = Edge('AB1')
        e2 = Edge('AB2')

        assert e1 != e2

    def test__repr__(self):
        e1 = Edge('AB1')
        assert repr(e1) == 'Edge(AB1)'

    def test_edge_len_must_be_numeric(self):
        with pytest.raises(ValueError) as valerror:
            e1 = Edge('ABZ')
        assert 'Edge length must be numeric' in str(valerror)
