import re
import os

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    # видалення пробілів та пустих рядків
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)

filename = 'text.txt'
current_directory = os.path.dirname(os.path.realpath(__file__))

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

words = count_words(text)
sentences = count_sentences(text)

result = 'result.txt'
with open(os.path.join(current_directory, result), 'w', encoding='utf-8') as output_file:
    output_file.write(f"Кількість слів = {words}\n")
    output_file.write(f"Кількість речень = {sentences}\n")