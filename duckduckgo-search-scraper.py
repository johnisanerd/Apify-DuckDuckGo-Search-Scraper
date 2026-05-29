"""
DuckDuckGo API: A Quick Start Example
See more at: https://apify.com/johnvc/DuckDuckGoSEOScraper?fpr=9n7kx3
Input schema: https://apify.com/johnvc/DuckDuckGoSEOScraper/input-schema?fpr=9n7kx3

This script shows how to call the DuckDuckGo API on Apify from Python and read its
structured JSON output. It exercises several input parameters so you can see what
is configurable, while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one query, max_pages=1) to keep this first run
# inexpensive. Raise these once you have your own API key and know your budget.
run_input = {
    "query": "machine learning",   # the only required field
    "localization": "us-en",        # 40+ region-language codes, e.g. uk-en, fr-fr, de-de
    "safe": "moderate",             # strict, moderate, or off
    # "date_filter": "w",           # d, w, m, y, or a custom YYYY-MM-DD..YYYY-MM-DD range
    "max_pages": 1,                 # pages to fetch; kept at 1 to keep the run cheap
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/DuckDuckGoSEOScraper").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset (one item per page)
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} item(s).\n")

# Show a few key fields from each page of results.
for item in items:
    print(
        f"Query: {item.get('query')}  |  "
        f"Page: {item.get('page_number')}  |  "
        f"Results found: {item.get('total_results_found')}"
    )
    for result in (item.get("organic_results") or [])[:5]:
        print(f"  {result.get('position')}. {result.get('title')}")
        print(f"     {result.get('link')}")
    print()
