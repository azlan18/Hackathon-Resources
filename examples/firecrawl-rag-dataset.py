#!/usr/bin/env python
"""
Firecrawl + RAG Dataset Creation
Personal experience: Used for building knowledge bases from documentation
"""

import os
from firecrawl import Firecrawl
import json

# Initialize Firecrawl
firecrawl = Firecrawl(api_key=os.getenv("FIRECRAWL_API_KEY"))

def crawl_documentation(base_url: str, max_pages: int = 50) -> list:
    """
    Crawl entire documentation site and return markdown pages
    
    Args:
        base_url: Starting URL to crawl
        max_pages: Maximum pages to crawl
    
    Returns:
        List of documents with markdown content
    """
    print(f"Starting crawl of {base_url}...")
    
    # Crawl the entire site
    response = firecrawl.crawl(
        base_url,
        limit=max_pages,
        scrape_options={
            "formats": ["markdown"],
            "onlyMainContent": True,  # Skip nav, footer, etc.
        }
    )
    
    documents = []
    for page in response:
        documents.append({
            "url": page.get("url"),
            "title": page.get("title"),
            "content": page.get("markdown"),
            "metadata": {
                "word_count": len(page.get("markdown", "").split()),
                "source": base_url
            }
        })
    
    print(f"Crawled {len(documents)} pages")
    return documents

def save_for_rag(documents: list, output_file: str = "rag_dataset.json"):
    """
    Save crawled documents in RAG-ready format
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(documents, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(documents)} documents to {output_file}")
    
    # Print stats
    total_words = sum(doc["metadata"]["word_count"] for doc in documents)
    print(f"Total words: {total_words:,}")
    print(f"Avg words per page: {total_words // len(documents):,}")

if __name__ == "__main__":
    # Example: Crawl a documentation site
    docs = crawl_documentation(
        "https://docs.python.org/3/tutorial/",
        max_pages=30
    )
    
    save_for_rag(docs)
    
    # Now use with LangChain/LlamaIndex for RAG!
    print("\nReady to use with RAG frameworks:")
    print("- Load JSON into LangChain DocumentLoader")
    print("- Create embeddings with OpenAI/HuggingFace")
    print("- Store in Chroma/Pinecone vector DB")
