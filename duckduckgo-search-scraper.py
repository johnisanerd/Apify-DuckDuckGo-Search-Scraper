"""
DuckDuckGo Search Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/apifyduckduckgo?fpr=9n7kx3

This script demonstrates how to use the DuckDuckGo Search Scraper Actor
to search DuckDuckGo and retrieve structured search results.
"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input:  Search the query, set the localization to US English, set the safe search to moderate, and set the maximum number of pages to 2.
run_input = {
    "query": "scrape duckduckgo with python tutorial",
    "localization": "us-en",
    "safe": "moderate",
    "max_pages": 2,
}

# Run the Actor and wait for it to finish
run = client.actor("drYfVwbtEdPqbFkiC").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)