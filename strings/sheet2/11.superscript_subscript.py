def superscript_subscript(text: str) -> str:
    superscript_map = str.maketrans({
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    })
    return text.replace("2", "2".translate(superscript_map))

result = superscript_subscript("E = mc2")
