import re

def detect_urls(s):
    return re.findall(r"https?://[\w\-\.]+(?:/[^\s]*)?", s)

result = detect_urls("Check this link: https://openai.com and http://github.com")  # ['https://openai.com', 'http://github.com']
