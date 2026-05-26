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

## Using with MCP

This scraper is the Apify Actor **[johnvc/DuckDuckGoSEOScraper](https://apify.com/johnvc/DuckDuckGoSEOScraper?fpr=9n7kx3)**. For AI assistants, Apify hosts an MCP server where you can **preload only this Actor** so the tool list stays small.

### Install via the Apify MCP configurator (use this link)

Everything below is also spelled out interactively on Apify’s MCP setup page for this Actor — **pick your app under “Client setup”** and follow that tab’s steps (each client has its own flow: connectors, JSON paths, CLI, IDE files, etc.).

**[https://mcp.apify.com/?tools=johnvc/DuckDuckGoSEOScraper](https://mcp.apify.com/?tools=johnvc/DuckDuckGoSEOScraper)**

On that page you get:

| Section | What it’s for |
|--------|----------------|
| **MCP server URL** | Copy/paste connection URL for agents that ask for a server URL. |
| **Client setup** | Tabbed instructions per client — **Claude Desktop**, **Claude.ai**, **Claude Code**, plus **Cursor**, **VS Code**, **ChatGPT**, **Codex CLI**, **Antigravity**, **Kiro**, and others under “More”. |

**Auth:** use **[OAuth](https://docs.apify.com/platform/integrations/mcp)** in the browser when offered, or your **[Apify API token](https://console.apify.com/settings/integrations)** (same kind of secret as `APIFY_API_TOKEN` in this repo). The configurator lets you choose token vs OAuth where applicable.

**Canonical MCP URL for this Actor:**

```text
https://mcp.apify.com/?tools=johnvc/DuckDuckGoSEOScraper
```

### What the configurator shows (examples)

These mirror [the page above](https://mcp.apify.com/?tools=johnvc/DuckDuckGoSEOScraper); use the live tabs for full detail.

**Claude.ai**

1. **Customize → Connectors → Browse connectors**, search for **Apify MCP server**, install, enable/update if prompted.
2. When connecting, use your API token and enabled tools: `johnvc/DuckDuckGoSEOScraper`.
3. In chat: **+ → Connectors →** turn on **Apify**.
4. Alternatively: **Add custom connector** with the full MCP URL and OAuth — see the Claude.ai tab on the configurator.

**Claude Desktop**

1. **Settings → Developer → Edit Config** and edit `claude_desktop_config.json`:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Optional: add Apify API token in the UI; if you skip it, **OAuth** is used by default.
3. Example remote config (same pattern as the configurator — `mcp-remote` + your Actor-specific URL):

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=johnvc/DuckDuckGoSEOScraper"
      ]
    }
  }
}
```

More help: [Claude Desktop + Apify](https://docs.apify.com/platform/integrations/claude-desktop).

**Cursor, Claude Code, VS Code, ChatGPT, Codex CLI, …**

Open the **[same configurator link](https://mcp.apify.com/?tools=johnvc/DuckDuckGoSEOScraper)**, select the **Client setup** tab for your tool, and copy the steps there (for example Cursor `.cursor/mcp.json`, or Claude Code `claude mcp add --transport http …`). Reference docs: [Apify MCP](https://docs.apify.com/platform/integrations/mcp) · [Claude Code MCP](https://code.claude.com/docs/en/mcp).

### Quick reference (optional)

**Cursor** — project `.cursor/mcp.json`, `url` set to the canonical MCP URL above; add `headers.Authorization: Bearer …` if you use token auth instead of OAuth.

**Claude Code**

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=johnvc/DuckDuckGoSEOScraper"
```

With token:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=johnvc/DuckDuckGoSEOScraper" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then run `claude mcp list` or `/mcp` in-session.

### Running this scraper from chat

Use inputs like [Usage Examples](#usage-examples) (`query`, `localization`, `safe`, `date_filter`, `max_pages`, …). The sample script uses Actor ID `drYfVwbtEdPqbFkiC`; on MCP the Store id is `johnvc/DuckDuckGoSEOScraper`.



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

Last Updated: 2026.05.27
