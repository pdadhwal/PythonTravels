import pytest
from kiwiland.spec_routes import DistanceRouteSpec

from kiwiland.exceptions import InvalidRouteSpecError


class TestExtractDistanceRouteSpec:
    @pytest.fixture
    def route_spec(self):
        return [
            ("1. The distance of the route A-B-C.", 'A-B-C'),
            ("2. The distance of the route A-D.", 'A-D'),
            ("3. The distance of the route A-D-C.", 'A-D-C'),
            ("4. The distance of the route A-E-B-C-D.", 'A-E-B-C-D'),
        ]

    def test_route_with_spec(self, route_spec):
        for route, expected_answer in iter(route_spec):
            extractor = DistanceRouteSpec(route)
            assert extractor.route == expected_answer
            assert extractor.testid is not None

    def test_bad_route_spec(self):
        with pytest.raises(InvalidRouteSpecError):
            extractor = DistanceRouteSpec('The quick brown foxy lady!')
