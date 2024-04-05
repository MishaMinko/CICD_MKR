import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

filename = 'text.txt'

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()