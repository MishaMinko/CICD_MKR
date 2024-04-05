import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    # видалення пробілів та пустих рядків
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)

filename = 'text.txt'

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

words = count_words(text)
sentences = count_sentences(text)

print("Кількість слів:", words)
print("Кількість речень:", sentences)