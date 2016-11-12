from kiwiland.bfs import bfs_paths
from kiwiland.route import Route


def shortest_path(graph, start, goal):
    try:
        routes = set()
        for path in bfs_paths(graph, start, goal):
            route_spec = '-'.join(path)
            route = Route(graph, route_spec)
            routes.add(route)

        return min(routes, key=lambda x: x.distance)
    except ValueError:
        return None
