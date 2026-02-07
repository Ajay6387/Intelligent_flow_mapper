
from collections import defaultdict

class NavigationGraph:
    def __init__(self):
        self.edges = defaultdict(set)
        self.link_frequency = defaultdict(int)
        self.pages = set()

    def add_page(self, url):
        self.pages.add(url)

    def add_edge(self, src, dst):
        self.edges[src].add(dst)
        self.link_frequency[dst] += 1

    def prune_global_links(self, threshold):
        total_pages = len(self.pages)
        global_links = {
            link for link, freq in self.link_frequency.items()
            if total_pages and freq / total_pages >= threshold
        }

        for src in list(self.edges.keys()):
            self.edges[src] -= global_links

        return global_links

    def to_json(self):
        return {
            "nodes": list(self.pages),
            "edges": [
                {"from": src, "to": dst}
                for src, targets in self.edges.items()
                for dst in targets
            ]
        }
