
import asyncio
import aiohttp
import sys
import json

from config import CrawlConfig
from crawler import CrawlerEngine
from url_manager import URLManager
from graph import NavigationGraph

async def crawl(start_url):
    config = CrawlConfig()
    crawler = CrawlerEngine(config)
    manager = URLManager()
    graph = NavigationGraph()

    manager.add(start_url, 0)

    async with aiohttp.ClientSession() as session:
        while manager.queue:
            url, depth = manager.get()

            if url in manager.visited or depth > config.max_depth:
                continue

            manager.visited.add(url)
            graph.add_page(url)

            html = await crawler.fetch(session, url)
            if not html:
                continue

            links = crawler.extract_links(url, html)

            for link in links:
                graph.add_edge(url, link)
                manager.add(link, depth + 1)

    graph.prune_global_links(config.global_link_threshold)
    return graph.to_json()

if __name__ == "__main__":
    start_url = sys.argv[1]
    result = asyncio.run(crawl(start_url))
    print(json.dumps(result, indent=2))
