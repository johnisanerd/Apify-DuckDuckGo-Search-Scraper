 https://apify.com/johnvc/DuckDuckGoSEOScraper?fpr=9n7kx3

# 🚀 DuckDuckGo Search Scraper

> **The most efficient, reliable, and developer-friendly DuckDuckGo search scraper**

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- An Apify account and API key

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnvc/Apify-DuckDuckGo-Search-Scraper.git
   cd Apify-DuckDuckGo-Search-Scraper
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Using venv (Python 3.3+)
   python -m venv venv
   
   # Activate the virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Install from requirements.txt
   pip install -r requirements.txt

   ```

4. **Configure your API key**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Apify API key
   # Get your API key from: https://apify.com?fpr=9n7kx3
   ```

5. **Run the example**
   ```bash
   python duckduckgo-search-scraper.py
   ```

### Alternative: Direct API Key Usage
If you prefer not to use a `.env` file, you can set the environment variable directly:
```bash
export APIFY_API_TOKEN="your_api_key_here"
python duckduckgo-search-scraper.py
```



# 🌟 Why Choose This Scraper?

> **The most efficient, reliable, and developer-friendly DuckDuckGo search scraper**

The DuckDuckGo Search data scraper delivers enterprise-grade performance with these advanced capabilities:

**Performance & Reliability**: Built optimized for high-throughput scraping with intelligent rate limiting and pagination handling.

**Cost-Effective**: Provides consistent, reliable results with intelligent pagination management to optimize API usage.

**Lightning-Fast Search & Retrieval**: Search any keyword across DuckDuckGo with blazing-fast performance. Retrieve comprehensive results in seconds, not minutes, with intelligent caching and optimization.

**Precision Targeting & Advanced Filtering**: Pinpoint exact search parameters with localization support, safe search filtering, and date filtering. Get precisely the search data you need, when you need it.

**Rich, Structured Data Extraction**: Extract complete search information, including organic results, ads, knowledge graph, news results, inline images, inline videos, and related searches. Our advanced parsing ensures you get clean, structured data ready for immediate use.

**Enterprise-Grade Configuration & Flexibility**: Built for developers and businesses who demand reliability. Highly configurable with intuitive controls, comprehensive error handling, and robust logging. Focus on your business logic while we handle the complexity of search scraping.

**No Hidden Costs or Rental Fees**: We do not charge monthly rentals, our scraper operates on a pay-per-use model. Scale up or down based on your actual needs without being locked into expensive subscriptions.

## 🚀 Features

### Core Capabilities
- **Advanced Search**: Support for complex queries with localization, safe search filtering, and date filtering
- **Intelligent Pagination**: Automatic handling of DuckDuckGo search pagination with configurable limits
- **Global Localization**: Support for 40+ international regions and languages
- **Safe Search Control**: Configurable content filtering (Strict, Moderate, Off)
- **Date Filtering**: Advanced time-based result filtering using predefined periods and custom date ranges

### Data Quality
- **Clean Output**: Automatic structured data metadata for clean, production-ready data
- **Structured Results**: Consistent JSON structure across all search results
- **Comprehensive Fields**: Organic results, ads, knowledge graph, news, inline images, inline videos, and related searches
- **Metadata Tracking**: Page-level analytics and search performance metrics
- **Per-Page Billing**: Results are pushed as separate dataset items for accurate billing

## 📖 Usage Examples

### Basic Search Example

Search for "python tutorial" with default settings.

```json
{
  "query": "python tutorial"
}
```

### Advanced Search Example

Search for "machine learning" with UK localization, strict safe search, past week filtering, and pagination limits.

```json
{
  "query": "machine learning",
  "localization": "uk-en",
  "safe": "strict",
  "date_filter": "w",
  "max_pages": 3
}
```

## 🔍 Input References

#### Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `str` | ✅ | `"python tutorial"` | Search query |
| `localization` | `str` | ❌ | `"us-en"` | Region and language code (e.g., `"uk-en"` for UK English, `"fr-fr"` for French) |
| `safe` | `str` | ❌ | `"moderate"` | Safe search level (`"strict"`, `"moderate"`, or `"off"`) |
| `date_filter` | `Optional[str]` | ❌ | `None` | Date filter format (`"d"` for past day, `"w"` for past week, `"m"` for past month, `"y"` for past year, or custom `"YYYY-MM-DD..YYYY-MM-DD"`) |
| `max_pages` | `Optional[int]` | ❌ | `2` | Maximum pages to fetch (0 = no limit) |
| `output_file` | `Optional[str]` | ❌ | `None` | Custom output filename |

## 📊 Output Format

### Search Result Structure

```json
{
  "query": "machine learning",
  "localization": "uk-en",
  "safe_search": 1,
  "date_filter": "w",
  "max_pages": 3,
  "total_results_found": 150,
  "pages_processed": 3,
  "search_metadata": {
    "localization": "uk-en",
    "localization_name": "United Kingdom (English)",
    "safe_search": 1,
    "safe_search_description": "Strict",
    "date_filter": "w",
    "max_pages": 3,
    "pagination_limit_reached": false
  },
  "pagination_info": {
    "total_pages": 3,
    "max_pages_set": 3,
    "pagination_stopped_by_limit": false,
    "results_per_page": {
      "first_page": 30,
      "subsequent_pages": 50
    }
  },
  "organic_results": [
    {
      "title": "Machine Learning Tutorial",
      "link": "https://example.com/ml-tutorial",
      "snippet": "Learn machine learning fundamentals...",
      "position": 1,
      "displayed_link": "example.com",
      "thumbnail": "https://thumbnail.url",
      "favicon": "https://favicon.url",
      "date": "2024-01-15",
      "rich_snippet": "Rich snippet content...",
      "sitelinks": [...]
    }
  ],
  "ads": [...],
  "knowledge_graph": [...],
  "news_results": [...],
  "inline_images": [...],
  "inline_videos": [...],
  "related_searches": [...],
  "results_by_page": {
    "1": {
      "organic_results": [...],
      "ads": [...],
      "knowledge_graph": [...],
      "news_results": [...],
      "inline_images": [...],
      "inline_videos": [...],
      "related_searches": [...]
    }
  }
}
```


[**Made with ❤️**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your search automation with the most reliable and efficient DuckDuckGo search scraper on the market.*

Last Updated: 2026.02.16
