# Using the Firecrawl plugin in Cursor

The Firecrawl plugin wires Cursor to **Firecrawl’s CLI** for web search, scraping, mapping, crawling, and related tasks. The bundled agent skill steers the AI to prefer `firecrawl` over generic “fetch the URL” tools when something needs the live web.

## What it gives you

Web work goes through Firecrawl: search, scrape pages, map sites, crawl, optional browser automation, and agent-style extraction. Output is tuned for LLM context (e.g. clean markdown, JS-rendered pages where supported).

## One-time setup

1. **Install the CLI** (global npm):

   ```bash
   npm install -g firecrawl-cli
   ```

2. **Check it’s ready**:

   ```bash
   firecrawl --status
   ```

   You want to see authentication (e.g. via `FIRECRAWL_API_KEY`) and credit/concurrency info.

3. **Sign in** if needed:

   ```bash
   firecrawl login --browser
   ```

   Or use an API key from [firecrawl.dev](https://firecrawl.dev): `firecrawl login --api-key "<key>"` or `export FIRECRAWL_API_KEY="<key>"`.

If `firecrawl` isn’t found, fix npm global `PATH` or try `npx firecrawl-cli`.

## How you use it

**In chat:** Ask for things that need the web in normal language (“search for…”, “pull the docs from…”, “what does X’s API say about…”). With the plugin/skill enabled, the agent is steered to run **`firecrawl`** commands.

**On the command line:** Run `firecrawl` in the integrated terminal; use **`-o`** to write results to files so large output doesn’t flood the chat.

**Where to put output:** Use a project folder like `.firecrawl/` and add it to `.gitignore` if you don’t want scraped files committed. **Quote URLs** in the shell (`?` and `&` are special).

## Command flow (what to use when)

1. **`search`** — No URL yet; discovery and research.  
   `search --scrape` already pulls page content for hits—don’t scrape those same URLs again unless you need more.

2. **`scrape`** — You have a URL; get markdown (or HTML/links, etc.). Use **`--wait-for <ms>`** if the page is JS-heavy.

3. **`map`** (often **`map --search "…"`**) — Large site; find the right path, then **`scrape`** that URL.

4. **`crawl`** — Many pages under a path/domain (use **`--wait`** when you need finished results).

5. **`browser`** — Only when interaction is required (pagination, forms). **Avoid** on heavy bot-detection sites (e.g. major search UIs); use **`firecrawl search`** for web search.

6. **`agent`** — Longer, AI-driven extraction (minutes); optional JSON schema for structured output.

### Examples

```bash
firecrawl search "your query" --json -o .firecrawl/search-topic.json
firecrawl search "your query" --scrape -o .firecrawl/search-topic-scraped.json
firecrawl scrape "https://example.com/docs" -o .firecrawl/example-docs.md
firecrawl map "https://docs.example.com" --search "auth" -o .firecrawl/map-auth.txt
```

## Credits and parallelism

- **`firecrawl credit-usage`** — See remaining credits.
- **`firecrawl --status`** — Concurrency limit; independent scrapes can run in parallel up to that limit.

## Reading output

Saved files can be large. Prefer **`head`**, **`grep`**, **`jq`**, or reading slices in the editor instead of loading the whole file into chat.

## Summary

Install and authenticate the **Firecrawl CLI**, then either run **`firecrawl … -o .firecrawl/...`** in the terminal or ask Cursor to do web research—the plugin/skill encourages a **search → scrape → map/crawl → browser** workflow instead of weaker alternatives.

For full CLI options (sources, categories, crawl limits, browser commands, etc.), see the Firecrawl skill bundled with the plugin or run `firecrawl --help`.
