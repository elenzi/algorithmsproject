from algorithmsproject.airport import Airport


class Route:
    """Represent an ordered list of airports"""

    def __init__(self):
        self.queue = []

    def enqueue(self, airport: Airport):
        self.queue.insert(0, airport)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def __repr__(self):
        return ' > '.join([str(a) for a in reversed(self.queue)])
