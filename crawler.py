
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from yarl import URL

class CrawlerEngine:
    def __init__(self, config):
        self.config = config

    async def fetch(self, session, url):
        try:
            async with session.get(url, timeout=self.config.timeout) as resp:
                if resp.status == 200:
                    return await resp.text()
        except Exception:
            return None

    def extract_links(self, base_url, html):
        soup = BeautifulSoup(html, "html.parser")
        links = set()
        base = URL(base_url)

        for a in soup.find_all("a", href=True):
            href = URL(a["href"])
            if not href.is_absolute():
                href = base.join(href)
            if href.host == base.host:
                links.add(str(href.with_fragment(None)))
        return links
