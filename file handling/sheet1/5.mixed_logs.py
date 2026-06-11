def summarize_mixed_logs(path: str) -> dict[str, int]:
    """Return a placeholder summary for mixed log files."""
    return {"path": path, "summary_lines": 0}

result = summarize_mixed_logs("mixed_logs.log")
