"""
MCP Tools Integration for Video Creator Agent
Adds web search capabilities via Tavily MCP or DuckDuckGo (free)
"""

import os
import json
from typing import Optional
from mcp_client import SSEMCPClient, create_mcp_client, mcp_tools_to_openai

# Try to import DuckDuckGo (free alternative)
try:
    from ddgs import DDGS
    DUCKDUCKGO_AVAILABLE = True
except ImportError:
    try:
        from duckduckgo_search import DDGS
        DUCKDUCKGO_AVAILABLE = True
    except ImportError:
        DUCKDUCKGO_AVAILABLE = False


# Tavily MCP client (lazy initialization)
_tavily_client = None
_tavily_tools = None


def get_tavily_client():
    """Get or create Tavily MCP client"""
    global _tavily_client

    if _tavily_client is None:
        # Check if Tavily is enabled
        if not os.environ.get("TAVILY_REMOTE_SSE_URL"):
            return None

        try:
            _tavily_client = SSEMCPClient(
                os.environ["TAVILY_REMOTE_SSE_URL"]
            )
            _tavily_client.initialize()
        except Exception as e:
            print(f"⚠️  Failed to connect to Tavily MCP: {e}")
            return None

    return _tavily_client


def get_tavily_tools():
    """Get Tavily MCP tools as OpenAI function definitions"""
    global _tavily_tools

    client = get_tavily_client()
    if client is None:
        return []

    if _tavily_tools is None:
        try:
            mcp_tools = client.list_tools()
            _tavily_tools = mcp_tools_to_openai(mcp_tools)
        except Exception as e:
            print(f"⚠️  Failed to list Tavily tools: {e}")
            return []

    return _tavily_tools


def tavily_search(query: str, max_results: int = 10) -> str:
    """
    Perform web search using Tavily MCP

    Args:
        query: Search query
        max_results: Maximum number of results

    Returns:
        Search results as formatted text
    """
    client = get_tavily_client()
    if client is None:
        return "❌ Tavily MCP is not available. Please set TAVILY_REMOTE_SSE_URL environment variable."

    try:
        result = client.call_tool("tavily-search", {
            "query": query,
            "max_results": max_results
        })
        # Check if result contains error messages
        if isinstance(result, str) and ("Invalid API key" in result or "error" in result.lower()):
            return f"❌ Tavily search failed: {result}"
        return result
    except Exception as e:
        return f"❌ Tavily search error: {str(e)}"


def tavily_extract(url: str) -> str:
    """
    Extract content from a web page using Tavily MCP

    Args:
        url: URL to extract content from

    Returns:
        Extracted content as text
    """
    client = get_tavily_client()
    if client is None:
        return "❌ Tavily MCP is not available."

    try:
        result = client.call_tool("tavily-extract", {
            "url": url
        })
        # Check if result contains error messages
        if isinstance(result, str) and ("Invalid API key" in result or "error" in result.lower()):
            return f"❌ Tavily extract failed: {result}"
        return result
    except Exception as e:
        return f"❌ Tavily extract error: {str(e)}"


# Tool definitions for agent integration
TAVILY_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for current information, trends, and facts using Tavily search engine. Returns relevant URLs and snippets.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query string"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 10)"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_webpage",
            "description": "Extract main content from a webpage URL. Useful for getting full article text, blog posts, or documentation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL of the webpage to extract content from"
                    }
                },
                "required": ["url"]
            }
        }
    }
]


# Enhanced tool implementations with MCP support
def web_search(query: str, max_results: int = 10) -> str:
    """
    Web search tool - tries Tavily MCP first, falls back to DuckDuckGo
    """
    # Try Tavily MCP first
    tavily_result = tavily_search(query, max_results)
    if not tavily_result.startswith("❌"):
        return tavily_result

    # Fallback to DuckDuckGo (free, no API key needed)
    if DUCKDUCKGO_AVAILABLE:
        try:
            ddgs = DDGS()
            results = ddgs.text(query, max_results=max_results)

            if not results:
                return f"❌ No results found for: {query}"

            output = [f"🔎 Search results for: {query}\n"]
            for i, result in enumerate(results, 1):
                output.append(f"\n{i}. {result.get('title', 'N/A')}")
                output.append(f"   URL: {result.get('href', result.get('link', 'N/A'))}")
                output.append(f"   {result.get('body', result.get('snippet', 'N/A'))}")

            return "\n".join(output)
        except Exception as e:
            return f"❌ DuckDuckGo search error: {str(e)}"

    return "❌ Web search not available. Install duckduckgo-search: pip install duckduckgo-search"


def extract_webpage(url: str) -> str:
    """
    Extract webpage content using Tavily MCP or simple request
    """
    # Try Tavily MCP first
    tavily_result = tavily_extract(url)
    if not tavily_result.startswith("❌"):
        return tavily_result

    # Fallback to simple extraction
    try:
        import requests
        from bs4 import BeautifulSoup

        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        text = soup.get_text()

        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # Return first 2000 characters
        if len(text) > 2000:
            text = text[:2000] + "\n\n... (truncated)"

        return f"📄 Content from {url}:\n\n{text}"
    except Exception as e:
        return f"❌ Failed to extract webpage: {str(e)}"


def cleanup_tavily_client():
    """Cleanup Tavily MCP client"""
    global _tavily_client, _tavily_tools

    if _tavily_client is not None:
        try:
            _tavily_client.close()
        except:
            pass

        _tavily_client = None
        _tavily_tools = None
