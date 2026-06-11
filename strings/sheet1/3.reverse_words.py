#!/usr/bin/env python3

def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

result = reverse_words("I love Python")  # "Python love I"
print(result)
