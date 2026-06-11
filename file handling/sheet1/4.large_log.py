def summarize_large_log(path: str) -> dict[str, int]:
    """Return a placeholder summary for a large log file."""
    return {"path": path, "summary_lines": 0}

result = summarize_large_log("large_log.txt")
