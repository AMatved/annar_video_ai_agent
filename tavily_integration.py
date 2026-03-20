"""
Tavily CLI Integration for Video Creator Agent
Fast web search using Tavily CLI (tvly command)
"""

import subprocess
import json
import os
from typing import Optional, Dict, Any


def tavily_cli_search(query: str, max_results: int = 10, **kwargs) -> str:
    """
    Perform web search using Tavily CLI (tvly command)
    Much faster than DuckDuckGo (~1 second vs ~35 seconds)

    Args:
        query: Search query string
        max_results: Maximum number of results to return
        **kwargs: Additional Tavily options (depth, time_range, etc.)

    Returns:
        Formatted search results as text
    """
    try:
        # Build command as string for shell=True
        cmd_parts = [
            "tvly",
            "search",
            f'"{query}"',  # Quote query to handle spaces
            "--max-results", str(max_results),
            "--json"
        ]

        # Add optional parameters
        if kwargs.get("depth") == "advanced":
            cmd_parts.extend(["--depth", "advanced"])

        if kwargs.get("time_range"):
            cmd_parts.extend(["--time-range", kwargs["time_range"]])

        if kwargs.get("topic"):
            cmd_parts.extend(["--topic", kwargs["topic"]])

        # Join command for shell execution
        cmd = " ".join(cmd_parts)

        # Add PATH for Windows
        env = os.environ.copy()
        tvly_path = r"C:\Users\User\AppData\Roaming\Python\Python313\Scripts"
        env["PATH"] = f"{tvly_path};{env.get('PATH', '')}"

        # Execute command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            env=env,
            timeout=30,
            shell=True  # Use shell=True for Windows
        )

        if result.returncode != 0:
            return f"❌ Tavily CLI error: {result.stderr}"

        # Parse JSON response
        data = json.loads(result.stdout)

        # Format results
        output = [f"🔎 Search results for: {query}\n"]

        if data.get("answer"):
            output.append(f"📌 {data['answer']}\n")

        results = data.get("results", [])
        if not results:
            return f"❌ No results found for: {query}"

        for i, item in enumerate(results, 1):
            output.append(f"\n{i}. {item.get('title', 'N/A')}")
            output.append(f"   URL: {item.get('url', 'N/A')}")
            output.append(f"   Score: {item.get('score', 0):.4f}")

            content = item.get('content', '')
            if content:
                # Truncate content if too long
                preview = content[:200] + "..." if len(content) > 200 else content
                output.append(f"   {preview}")

        return "\n".join(output)

    except subprocess.TimeoutExpired:
        return "❌ Tavily CLI timeout (30s)"
    except json.JSONDecodeError as e:
        return f"❌ Failed to parse Tavily response: {str(e)}"
    except Exception as e:
        return f"❌ Tavily CLI error: {str(e)}"


def tavily_cli_extract(url: str, **kwargs) -> str:
    """
    Extract content from webpage using Tavily CLI

    Args:
        url: URL to extract content from
        **kwargs: Additional options

    Returns:
        Extracted content as text
    """
    try:
        # Build command as string for shell=True
        cmd = f'tvly extract "{url}" --json'

        # Add PATH for Windows
        env = os.environ.copy()
        tvly_path = r"C:\Users\User\AppData\Roaming\Python\Python313\Scripts"
        env["PATH"] = f"{tvly_path};{env.get('PATH', '')}"

        # Execute command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            env=env,
            timeout=30,
            shell=True  # Use shell=True for Windows
        )

        if result.returncode != 0:
            return f"❌ Tavily CLI error: {result.stderr}"

        # Parse JSON response
        data = json.loads(result.stdout)

        # Format results
        output = [f"📄 Content from {url}\n"]

        if data.get("answer"):
            output.append(f"{data['answer']}\n")

        results = data.get("results", [])
        if results:
            for item in results:
                content = item.get('content', '')
                if content:
                    # Truncate if too long
                    preview = content[:3000] + "\n\n...(truncated)" if len(content) > 3000 else content
                    output.append(preview)

        return "\n".join(output)

    except subprocess.TimeoutExpired:
        return "❌ Tavily CLI timeout (30s)"
    except json.JSONDecodeError as e:
        return f"❌ Failed to parse Tavily response: {str(e)}"
    except Exception as e:
        return f"❌ Tavily CLI error: {str(e)}"


# Check if Tavily CLI is available and authenticated
def is_tavily_available() -> bool:
    """Check if Tavily CLI is installed and authenticated"""
    try:
        # Check if config exists first (faster check)
        config_path = os.path.expanduser("~/.tavily/config.json")
        if not os.path.exists(config_path):
            return False

        # Check if tvly command works
        env = os.environ.copy()
        tvly_path = r"C:\Users\User\AppData\Roaming\Python\Python313\Scripts"
        env["PATH"] = f"{tvly_path};{env.get('PATH', '')}"

        result = subprocess.run(
            ["tvly", "--version"],
            capture_output=True,
            env=env,
            timeout=5,
            shell=True  # Use shell=True for Windows
        )

        return result.returncode == 0

    except:
        return False


# Fallback: Try Tavily CLI first, then DuckDuckGo
def smart_web_search(query: str, max_results: int = 10, **kwargs) -> str:
    """
    Smart web search that tries Tavily CLI first (fast), then DuckDuckGo (free)

    Args:
        query: Search query
        max_results: Maximum results
        **kwargs: Additional options

    Returns:
        Search results
    """
    # Try Tavily CLI first (fast, ~1 second)
    if is_tavily_available():
        try:
            result = tavily_cli_search(query, max_results, **kwargs)
            if not result.startswith("❌"):
                return result
        except:
            pass

    # Fallback to DuckDuckGo (free, ~35 seconds)
    try:
        from mcp_tools import web_search as ddg_search
        return ddg_search(query, max_results)
    except:
        return "❌ Web search not available. Please install Tavily CLI or ensure mcp_tools.py is configured."


# Tool definitions for agent integration
TAVILY_CLI_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search_fast",
            "description": "Fast web search using Tavily CLI (~1 second). Returns relevant URLs, snippets, and relevance scores. Falls back to DuckDuckGo if Tavily unavailable.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query string"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results (default: 10)"
                    },
                    "depth": {
                        "type": "string",
                        "enum": ["basic", "advanced"],
                        "description": "Search depth (default: basic)"
                    }
                },
                "required": ["query"]
            }
        }
    }
]
