#!/usr/bin/env python
"""
Serper.dev Search API Example
Personal experience: Used for real-time data enrichment in apps
"""

import os
import requests
import json

class SerperSearch:
    """Wrapper for Serper.dev Google Search API"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("SERPER_API_KEY")
        self.base_url = "https://google.serper.dev"
    
    def search(self, query: str, num_results: int = 10) -> dict:
        """
        Perform Google search
        
        Args:
            query: Search query
            num_results: Number of results (10-100)
        
        Returns:
            Dict with organic results, knowledge graph, etc.
        """
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        
        payload = {
            "q": query,
            "num": num_results
        }
        
        response = requests.post(
            f"{self.base_url}/search",
            headers=headers,
            json=payload
        )
        
        return response.json()
    
    def news_search(self, query: str) -> list:
        """Search for news articles"""
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            f"{self.base_url}/news",
            headers=headers,
            json={"q": query}
        )
        
        return response.json().get("news", [])
    
    def image_search(self, query: str) -> list:
        """Search for images"""
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            f"{self.base_url}/images",
            headers=headers,
            json={"q": query}
        )
        
        return response.json().get("images", [])

# Example usage
if __name__ == "__main__":
    searcher = SerperSearch()
    
    # Regular search
    results = searcher.search("FastAPI tutorial", num_results=5)
    
    print("Top 5 results for 'FastAPI tutorial':\n")
    for i, result in enumerate(results.get("organic", []), 1):
        print(f"{i}. {result['title']}")
        print(f"   {result['link']}")
        print(f"   {result['snippet']}\n")
    
    # News search
    news = searcher.news_search("AI hackathon 2026")
    print("\nLatest news on AI hackathons:")
    for article in news[:3]:
        print(f"- {article['title']} ({article['source']})")
    
    # Use case: Enrich user queries in real-time
    print("\n--- Use Case: Real-time data enrichment ---")
    user_query = "latest React trends"
    search_data = searcher.search(user_query, num_results=3)
    
    # Extract just URLs and snippets for LLM context
    context = "\n".join([
        f"{r['title']}: {r['snippet']}"
        for r in search_data.get("organic", [])
    ])
    
    print(f"\nContext for LLM about '{user_query}':")
    print(context[:300] + "...")
