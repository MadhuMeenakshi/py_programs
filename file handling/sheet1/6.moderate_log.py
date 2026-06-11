def summarize_moderate_log(path: str) -> dict[str, int]:
    """Return a placeholder summary for a moderate log file."""
    return {"path": path, "summary_lines": 0}

result = summarize_moderate_log("moderate_log.txt")
