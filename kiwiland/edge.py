class Edge:
    def __init__(self, edge):
        if len(edge) < 3:
            raise ValueError("Edge must have atleast 3 elements. e.g AB4")

        if edge[0] == edge[1]:
            raise ValueError('Edge cannot start and end at the same node. e.g AA4 is invalid. AB4 is valid')

        if not edge[2:].isnumeric():
            raise ValueError('Edge length must be numeric')

        self.start = edge[0]
        self.end = edge[1]
        self.distance = int(edge[2:])

    def __str__(self):
        return "{0}{1}{2}".format(self.start, self.end, self.distance)

    def __repr__(self):
        return "Edge({0}{1}{2})".format(self.start, self.end, self.distance)

    def __lt__(self, other):
        return str(self) < str(other)
