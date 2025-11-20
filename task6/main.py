import time
import re
from collections import Counter

start = time.perf_counter()

with open('python_article.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.lower()

letters = re.findall(r'[a-z]', text)
letterCounts = Counter(letters)

words = re.findall(r'\b\w+\b', text)
wordCounts = Counter(words)

reportLines = []

reportLines.append(f'Загальна кількість слів: {len(words)}')
reportLines.append(f'Загальна кількість літер: {len(letters)}\n')

reportLines.append('Рейтинг літер:')
for char, count in letterCounts.items():
    reportLines.append(f'{char}: {count}')

reportLines.append('\nРейтинг слів:')
for word, count in wordCounts.items():
    reportLines.append(f'{word}: {count}')

duration = time.perf_counter() - start
reportLines.append(f'\nЧас витрачений на аналіз: {duration:.5f} секунд')

report = '\n'.join(reportLines)

print(report)

with open('analysis.txt', 'w', encoding='utf-8') as log:
    log.write(report)