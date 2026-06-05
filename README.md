# 🦆 DuckDuckGo API: Structured DuckDuckGo Search Results in Clean JSON

> The most efficient, reliable, and developer-friendly way to use the DuckDuckGo API.

**Actor page:** [apify.com/johnvc/DuckDuckGoSEOScraper](https://apify.com/johnvc/DuckDuckGoSEOScraper?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/DuckDuckGoSEOScraper/input-schema](https://apify.com/johnvc/DuckDuckGoSEOScraper/input-schema?fpr=9n7kx3)

The DuckDuckGo API runs a DuckDuckGo search for any query and returns clean, structured JSON. Each page of results comes back as one item with organic listings (title, link, snippet, position, sitelinks), ads, knowledge graph panels, news results, inline images, inline videos, and related searches, plus per-page metadata. It supports 40+ region and language combinations, safe-search levels, date filtering, and automatic pagination. Because DuckDuckGo does not personalize results, the output is consistent across runs.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-DuckDuckGo-Search-Scraper.git
   cd Apify-DuckDuckGo-Search-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python duckduckgo-search-scraper.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python duckduckgo-search-scraper.py
```

## Why Use This DuckDuckGo API?

**Full results-page coverage.** One call returns the whole DuckDuckGo results page as structured data: organic listings, ads, knowledge graph panels, news, inline images, inline videos, and related searches. You get the entire page, not just the organic links.

**Consistent, non-personalized snapshots.** DuckDuckGo does not personalize results, so repeated runs return comparable SERPs, which is ideal for ranking analysis and monitoring over time.

**Localized and filterable.** Target 40+ region and language combinations, set the safe-search level, and filter by date (past day, week, month, year, or a custom range).

**Predictable, pay-per-use pricing.** Billing is per run plus per page processed, with no monthly rental. You control cost directly with the page limit.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can run DuckDuckGo searches for you on demand.

## Features

### Core Capabilities
- **Keyword search** across DuckDuckGo with full results-page extraction
- **Localization** across 40+ region and language combinations
- **Safe-search control** (strict, moderate, or off)
- **Date filtering** with relative periods or a custom date range
- **Multi-page pagination** with a configurable page cap

### Data Quality
- **Structured organic results** with title, link, snippet, position, displayed link, date, and sitelinks
- **Rich result blocks**: ads, knowledge graph, news, inline images, inline videos, related searches
- **Per-page metadata** with result counts and pagination details
- **Consistent JSON** shape across every query
- **Per-page billing** so larger searches stay transparent

## Usage Examples

### Basic Example
A single-page search for one keyword. This is the cheapest way to try the API.
```json
{
  "query": "machine learning",
  "max_pages": 1
}
```

### Advanced Example
A UK-localized search with strict safe-search, results from the past week, and two pages.
```json
{
  "query": "machine learning",
  "localization": "uk-en",
  "safe": "strict",
  "date_filter": "w",
  "max_pages": 2
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `string` | Yes | - | The search query. |
| `localization` | `string` | No | `us-en` | Region and language code, e.g. `uk-en`, `fr-fr`, `de-de`, `ja-jp` (40+ supported). |
| `safe` | `string` | No | `moderate` | Safe-search level: `strict`, `moderate`, or `off`. |
| `date_filter` | `string` | No | (none) | `d` (past day), `w` (week), `m` (month), `y` (year), or a custom range `YYYY-MM-DD..YYYY-MM-DD`. |
| `max_pages` | `integer` | No | `2` | Maximum pages to fetch (`0` = no limit). |
| `output_file` | `string` | No | (none) | Optional filename to save results; auto-generated if omitted. |

## Output Format

A real dataset item for the query `machine learning`. Each page of results is one item; the first result's sitelinks are trimmed here for readability.

```json
{
  "query": "machine learning",
  "localization": "us-en",
  "safe_search": -1,
  "max_pages": 1,
  "search_timestamp": "2026-05-29T09:56:11.848097",
  "total_results_found": 11,
  "pages_processed": 1,
  "page_number": 1,
  "search_metadata": {
    "localization": "us-en",
    "localization_name": "United States (English)",
    "safe_search": -1,
    "safe_search_description": "Moderate",
    "max_pages": 1,
    "pagination_limit_reached": true
  },
  "pagination_info": {
    "total_pages": 1,
    "max_pages_set": 1,
    "pagination_stopped_by_limit": true,
    "results_per_page": { "first_page": 11, "subsequent_pages": 50 }
  },
  "organic_results": [
    {
      "position": 1,
      "title": "Machine Learning Tutorial - GeeksforGeeks",
      "link": "https://www.geeksforgeeks.org/machine-learning/machine-learning/",
      "date": "Apr 15, 2026",
      "snippet": "Machine learning is a branch of Artificial Intelligence that focuses on developing models and algorithms that let computers learn from data without being explicitly programmed for every task.",
      "favicon": "https://external-content.duckduckgo.com/ip3/www.geeksforgeeks.org.ico",
      "sitelinks": [
        {
          "title": "Gradient Descent in Linear Regression",
          "link": "https://www.geeksforgeeks.org/machine-learning/gradient-descent-in-linear-regression/"
        }
      ]
    },
    {
      "position": 2,
      "title": "Machine learning - Wikipedia",
      "link": "https://en.wikipedia.org/wiki/Machine_learning",
      "snippet": "Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data.",
      "favicon": "https://external-content.duckduckgo.com/ip3/en.wikipedia.org.ico"
    }
  ],
  "ads": [],
  "knowledge_graph": [],
  "news_results": [],
  "inline_images": [],
  "inline_videos": [],
  "related_searches": []
}
```

---

## Use as an MCP tool

You can load the DuckDuckGo API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/DuckDuckGoSEOScraper
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the DuckDuckGo API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/DuckDuckGoSEOScraper"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the DuckDuckGo API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/DuckDuckGoSEOScraper"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/DuckDuckGoSEOScraper" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the DuckDuckGo API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/DuckDuckGoSEOScraper`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/DuckDuckGoSEOScraper`, using OAuth when prompted.
5. Ask Claude to run the DuckDuckGo API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/DuckDuckGoSEOScraper"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/DuckDuckGoSEOScraper",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the DuckDuckGo API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/DuckDuckGoSEOScraper`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the DuckDuckGo API to power your search and SEO workflows with reliable, structured results.*

Last Updated: 2026.06.06
