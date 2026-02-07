
from dataclasses import dataclass

@dataclass
class CrawlConfig:
    max_depth: int = 2
    concurrency: int = 5
    timeout: int = 10
    global_link_threshold: float = 0.7
