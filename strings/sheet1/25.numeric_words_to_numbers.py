import re

WORD_TO_DIGIT = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def numeric_words_to_numbers(s):
    def replace(match):
        word = match.group(0).lower()
        return WORD_TO_DIGIT.get(word, word)
    return re.sub(r"\b(?:zero|one|two|three|four|five|six|seven|eight|nine)\b", replace, s, flags=re.IGNORECASE)

result = numeric_words_to_numbers("I have one apple and two oranges.")  # "I have 1 apple and 2 oranges."
