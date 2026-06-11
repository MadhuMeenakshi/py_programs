def replace_multiple_words(text: str, replacements: dict[str, str]) -> str:
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

result = replace_multiple_words(
    "I like apples and bananas.",
    {"apples": "oranges", "bananas": "grapes"}
)
