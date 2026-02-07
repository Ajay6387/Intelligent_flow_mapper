
from collections import deque

class URLManager:
    def __init__(self):
        self.visited = set()
        self.queue = deque()

    def add(self, url, depth):
        if url not in self.visited:
            self.queue.append((url, depth))

    def get(self):
        return self.queue.popleft() if self.queue else None
