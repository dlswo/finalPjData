import re

document_text = open('test.txt', 'rt', encoding='UTF8')
text_string = document_text.read().lower()
match_pattern = re.search(r'\b[a-z]{3,15}\b', text_string)
frequency = {}

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])