import pytest
from kiwiland.spec_routes import RoutesBetweenNodesWithMaxStopsSpec

from kiwiland.exceptions import InvalidRouteSpecError


class TestRoutesBetweenNodesWithMaxStopsSpec:
    def test_route_with_spec(self):
        spec = r'6. The number of trips starting at C and ending at C with a maximum of 3 stops.'
        extractor = RoutesBetweenNodesWithMaxStopsSpec(spec)

        assert extractor.testid == '6'
        assert extractor.start == 'C'
        assert extractor.end == 'C'
        assert extractor.num_stops == 3

    def test_bad_route_spec(self):
        with pytest.raises(InvalidRouteSpecError):
            extractor = RoutesBetweenNodesWithMaxStopsSpec('The quick brown foxy lady!')
