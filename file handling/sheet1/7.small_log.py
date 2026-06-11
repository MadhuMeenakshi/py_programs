def summarize_small_log(path: str) -> dict[str, int]:
    """Return a placeholder summary for a small log file."""
    return {"path": path, "summary_lines": 0}

result = summarize_small_log("small_log.txt")
