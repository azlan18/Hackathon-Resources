# Data & APIs

## Web Scraping

### Firecrawl
- **URL**: https://www.firecrawl.dev/
- **Features**:
  - Scrape: Single pages → markdown/HTML/structured data
  - Crawl: Entire websites recursively
  - Map: Get all URLs from a site (extremely fast)
  - Extract: AI-powered structured data extraction

**Python Example:**
```python
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# Scrape single page
doc = firecrawl.scrape("https://example.com", formats=["markdown", "html"])
print(doc.markdown)

# Crawl entire site
response = firecrawl.crawl(
    "https://example.com",
    limit=100,
    scrape_options={"formats": ["markdown", "html"]}
)
```

## Search APIs

### Serper.dev
- **URL**: https://serper.dev/
- **Free Credits**: 2,500+ queries for new signups
- **Speed**: 1-2 second response times
- **Pricing**: $0.30-$1.00 per 1,000 queries
- **Returns**: Organic results, images, videos, knowledge graphs, places

### Parallel.ai
- **URL**: https://parallel.ai/
- **Features**:
  - Deep Research Mode (48% accuracy vs GPT-4's 14%)
  - Multiple agent modes (fast, hyper-fast, comprehensive)
  - Scraping & page extraction
  - SOC 2 Type II certified

## Best Practices
- Use Firecrawl for creating RAG datasets or extracting clean data
- Use Serper for real-time search in your applications
- Use Parallel.ai when you need multi-hop reasoning and deep research
