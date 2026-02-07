
# Intelligent User Flow Mapper

## System Architecture Overview

This project implements an production-style backend service that crawls a website and
extracts an intelligent user navigation flow graph.

Core architectural principles:

- Modular components with strict separation of concerns
- Asynchronous crawling engine
- Heuristic-based navigation analysis
- Directed graph modeling
- JSON output optimized for UI visualization

## Components

1. Crawler Engine
   Asynchronous fetcher using aiohttp. Handles HTTP requests, retries, and rate limiting.

2. URL Manager
   Maintains visited URLs, crawl queue, and depth constraints.

3. Navigation Analyzer
   Extracts links and classifies global navigation using frequency heuristics.

4. Graph Builder
   Builds a directed navigation graph with noise-reduced edges.

5. Output Formatter
   Produces clean JSON representation for UI consumption.

## Heuristic Logic

- Links appearing on >70% of pages are classified as global navigation
- Footer/header patterns are detected using DOM similarity
- Repeated navigation edges are compressed

Limitations:

- SPA support is limited to static DOM after initial render
- Heuristics may misclassify heavily templated pages

## Running

```bash
pip install -r requirements.txt
python main.py https://example.com
```

## Future Improvements

- Headless browser rendering
- ML-based navigation clustering
- Persistent crawl cache
